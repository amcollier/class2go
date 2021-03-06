from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response, redirect, HttpResponseRedirect
from django.template import Context, loader
from c2g.models import Course, Video, VideoToExercise, Exercise

from c2g.models import Course, Video, VideoActivity
from courses.common_page_data import get_common_page_data
from courses.course_materials import get_course_materials
import datetime
from courses.videos.forms import *
import gdata.youtube
import gdata.youtube.service
from django.db.models import Q

from django.template import RequestContext
from courses.actions import auth_view_wrapper

@auth_view_wrapper
def list(request, course_prefix, course_suffix):
    try:
        common_page_data = get_common_page_data(request, course_prefix, course_suffix)
    except:
        raise Http404

    if 'id' in request.GET:
        #process Video model instance with this youtube id
        #and other stuff
        video = Video.objects.get(pk=request.GET['vid'])
        video.url = request.GET['id']
        video.save()
        video.create_production_instance()

    section_structures = get_course_materials(common_page_data=common_page_data, get_video_content=True)

    return render_to_response('videos/'+common_page_data['course_mode']+'/list.html', {'common_page_data': common_page_data, 'section_structures':section_structures, 'context':'video_list'}, context_instance=RequestContext(request))

@auth_view_wrapper
def view(request, course_prefix, course_suffix, slug):
    try:
        common_page_data = get_common_page_data(request, course_prefix, course_suffix)
    except:
        raise Http404

    video = None
    video_rec = None
    if request.user.is_authenticated():
        #video = Video.objects.get(course=common_page_data['production_course'], slug=slug)
        video = Video.objects.get(course=common_page_data['course'], slug=slug)
        #video_rec = request.user.videoactivity_set.filter(video=video)
        video_rec = request.user.videoactivity_set.filter(video=video)
        if video_rec:
            video_rec = video_rec[0]
        else:
            #if student, needs to be an easy way to check if member of group
            user_groups = request.user.groups.all()
            for group in user_groups:
                if group == common_page_data['course'].student_group:
                    video_rec = VideoActivity(student=request.user, course=common_page_data['course'], video=video)
                    video_rec.save()
                    break

    return render_to_response('videos/view.html', {'common_page_data': common_page_data, 'video': video, 'video_rec':video_rec}, context_instance=RequestContext(request))

@auth_view_wrapper
def edit(request, course_prefix, course_suffix, slug):
    try:
        common_page_data = get_common_page_data(request, course_prefix, course_suffix)
    except:
        raise Http404

    video = common_page_data['course'].video_set.all().get(slug=slug)
    form = S3UploadForm(course=common_page_data['course'], instance=video)

    return render(request, 'videos/edit.html',
            {'common_page_data': common_page_data,
             'slug': slug,
             'form': form,
             })

def GetOAuth2Url(request):
    client_id = "287022098794.apps.googleusercontent.com"
    redirect_uri = "http://" + request.META['HTTP_HOST'] + "/oauth2callback"
    response_type = "code"
    scope = "https://gdata.youtube.com"

    return "https://accounts.google.com/o/oauth2/auth?client_id=" + client_id + "&redirect_uri=" + redirect_uri + "&scope=" + scope + "&response_type=" + response_type

@auth_view_wrapper
def upload(request, course_prefix, course_suffix):
    try:
        common_page_data = get_common_page_data(request, course_prefix, course_suffix)
    except:
        raise Http404

    data = {'common_page_data': common_page_data}

    form = S3UploadForm(course=common_page_data['course'])
    data['form'] = form

    return render_to_response('videos/s3upload.html',
                              data,
                              context_instance=RequestContext(request))


@auth_view_wrapper
def model_exercises(request, course_prefix, course_suffix, video_slug):
    #Get all necessary information about the problemset
    try:
        common_page_data = get_common_page_data(request, course_prefix, course_suffix)
    except:
        raise Http404
    data = {'common_page_data': common_page_data}
    form = ManageExercisesForm(initial={'course':common_page_data['course'].id})
    video = Video.objects.getByCourse(common_page_data['course']).get(slug=video_slug)
    videoToExs = VideoToExercise.objects.filter(video__course=common_page_data['course'], is_deleted=False, video__slug=video_slug).order_by('video_time')
    used_exercises = []
    exercise_attempted = False
#    if len(VideoActivity.objects.filter(video_to_exercise__video=video.image)) > 0:
#        exercise_attempted = True
    #Get the list of exercises currently in this problem set
    for videoToEx in videoToExs:
        used_exercises.append(videoToEx.exercise.id)
    #Get all the exercises in the course but not in this problem set to list in add from existing
    #Q objects allow queryset objects to be ORed together
    exercises = Exercise.objects.all().filter(Q(problemSet__course=common_page_data['course'])|Q(video__course=common_page_data['course'])).exclude(id__in=used_exercises).distinct()

    #Form processing action if form was submitted
    if request.method == 'POST':
        form = ManageExercisesForm(request.POST, request.FILES)
        if form.is_valid():
            video = Video.objects.get(id=request.POST['video_id'])
            file_content = request.FILES['file']
            file_name = file_content.name

            exercise = Exercise()
            exercise.handle = request.POST['course_prefix'] + '#$!' + request.POST['course_suffix']
            exercise.fileName = file_name
            exercise.file.save(file_name, file_content)
            exercise.save()

            video_time = request.POST['video_time']
            videoToEx = VideoToExercise(video=video, exercise=exercise, video_time=video_time, is_deleted=0, mode='staging')
            videoToEx.save()
            return HttpResponseRedirect(reverse('courses.videos.views.model_exercises', args=(request.POST['course_prefix'], request.POST['course_suffix'], video.slug,)))

    #If form was not submitted then the form should be displayed or if there were errors the page needs to be rendered again
    data['form'] = form
    data['course_prefix'] = course_prefix
    data['course_suffix'] = course_suffix
    data['video'] = video
    data['videoToExs'] = videoToExs
    data['exercise_attempted'] = exercise_attempted
    data['exercises'] = exercises
    return render_to_response('videos/model_exercises.html', data, context_instance=RequestContext(request))


@auth_view_wrapper
def manage_exercises(request, course_prefix, course_suffix, video_slug):
    try:
        common_page_data = get_common_page_data(request, course_prefix, course_suffix)
    except:
        raise Http404
    video = Video.objects.get(course=common_page_data['course'], slug=video_slug)
    videoToExs = VideoToExercise.objects.select_related('exercise', 'video').filter(video=video).order_by('video_time')
    added_exercises = video.exercise_set.all()
    exercises = Exercise.objects.filter(video__course=common_page_data['course']).exclude(id__in=added_exercises).distinct()
    return render_to_response('videos/manage_exercises.html',
                            {'request': request,
                                'common_page_data': common_page_data,
                                'course_prefix': course_prefix,
                                'course_suffix': course_suffix,
                                'video': video,
                                'videoToExs': videoToExs,
                                'exercises': exercises
                            },
                            context_instance=RequestContext(request))

@auth_view_wrapper
def add_exercise(request):
#    try:
#        common_page_data = get_common_page_data(request, course_prefix, course_suffix)
#    except:
#        raise Http404

    video = Video.objects.get(id=request.POST['video_id'])
    video_time = request.POST['videotime']

    file_content = request.FILES['exercise']
    file_name = file_content.name

    exercise = Exercise()
    exercise.handle = request.POST['course_prefix'] + '#$!' + request.POST['course_suffix']
    exercise.fileName = file_name
    exercise.file.save(file_name, file_content)
    exercise.save()

    index = len(video.exercise_set.all())
    videoToEx = VideoToExercise(video=video, exercise=exercise, is_deleted=False, video_time=video_time)
    videoToEx.save()
    return HttpResponseRedirect(reverse('courses.videos.views.manage_exercises', args=(request.POST['course_prefix'], request.POST['course_suffix'], video.slug,)))

@auth_view_wrapper
def add_existing_exercises(request):
    video = Video.objects.get(id=request.POST['video_id'])
    exercise_ids = request.POST.getlist('exercise')
    exercises = Exercise.objects.filter(id__in=exercise_ids)
    for exercise in exercises:
        video_time = request.POST['videotime_' + str(exercise.id)]
        videoToEx = VideoToExercise(video=video, exercise=exercise, number=len(video.exercise_set.all()), is_deleted=False, video_time=video_time)
        videoToEx.save()
    return HttpResponseRedirect(reverse('courses.videos.views.manage_exercises', args=(request.POST['course_prefix'], request.POST['course_suffix'], video.slug,)))

@auth_view_wrapper
def save_exercises(request):
    video = Video.objects.get(id=request.POST['video_id'])
 #   videoToEx = video.videotoexercise_set.all().order_by('number')
 #   for n in range(0,len(videoToEx)):
 #       listName = "exercise_order[" + str(n) + "]"
 #       videoToEx[n].number = request.POST[listName]
 #       videoToEx[n].save()
    return HttpResponseRedirect(reverse('courses.videos.views.manage_exercises', args=(request.POST['course_prefix'], request.POST['course_suffix'], video.slug,)))


@auth_view_wrapper
def get_video_exercises(request):
    video = Video.objects.get(id = request.GET['video_id'])
    videoToExs = VideoToExercise.objects.select_related('exercise', 'video').filter(video=video).order_by('video_time')
    json_list = []
    for videoToEx in videoToExs:
        json_string = "\"" + str(videoToEx.video_time) + "\": {\"time\": " + str(videoToEx.video_time) + ", \"problemDiv\": \"" + str(videoToEx.exercise_id) + "\"}"
        json_list.append(json_string)

    json_string = "{" + ','.join( map( str, json_list )) + "}"
    return HttpResponse(json_string)

@auth_view_wrapper
def load_video_problem_set(request, course_prefix, course_suffix, video_id):
    try:
        common_page_data = get_common_page_data(request, course_prefix, course_suffix)
    except:
        raise Http404

    ex_list = Exercise.objects.filter(videotoexercise__video_id=video_id)
    file_names = []
    for ex in ex_list:
        #Remove the .html from the end of the file name
        file_names.append(ex.fileName[:-5])
    # assessment type is hard-coded because all in-video exercises are formative
    return render_to_response('problemsets/load_problem_set.html',{'file_names': file_names, 'assessment_type': 'formative'},context_instance=RequestContext(request))
