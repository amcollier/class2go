from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, loader
from django.template import RequestContext
from courses.common_page_data import get_common_page_data
from courses.actions import auth_view_wrapper
from courses.forums.forms import PiazzaAuthForm
from main.database import PIAZZA_ENDPOINT, PIAZZA_KEY, PIAZZA_SECRET
from OAuthSimple import OAuthSimple

@auth_view_wrapper
def view(request, course_prefix, course_suffix):
    try:
        common_page_data = get_common_page_data(request, course_prefix, course_suffix)
    except:
        raise Http404

    # Only use the production course (for the piazza_id) since Piazza has no notion
    # of draft/live.
    course = common_page_data['production_course']

    lti_params = {
        "lti_message_type": "basic-lti-launch-request",
        "lti_version": "LTI-1p0",
        "resource_link_id": "class2go-forum",
    }
    lti_params['user_id'] = request.user.id
    lti_params['lis_person_name_given'] = request.user.first_name
    lti_params['lis_person_name_family'] = request.user.last_name
    lti_params['lis_person_name_full'] = request.user.first_name + " " + request.user.last_name
    lti_params['lis_person_contact_email_primary'] = request.user.email

    # Piazza only supports two roles, instructor and strudent.  TA's (readonly too) are instructors too. 
    if common_page_data['is_course_admin']:
        lti_params['roles'] = "Instructor"
    else:
        lti_params['roles'] = "Student"

    lti_params['context_id'] = course.piazza_id
    lti_params['context_label'] = common_page_data['course_prefix']
    lti_params['context_title'] = course.title

    # Use OAuthSimple to sign the request. 
    signatures = {
        'consumer_key': PIAZZA_KEY,
        'shared_secret': PIAZZA_SECRET,
    }
    oauthsimple = OAuthSimple()
    signed_request = oauthsimple.sign({
        'path': PIAZZA_ENDPOINT,
        'action': "POST",
        'parameters': lti_params, 
        'signatures': signatures,
    })

    form = PiazzaAuthForm(initial=signed_request['parameters'])

    return render_to_response('forums/piazza.html', {
            'common_page_data': common_page_data, 
            'form': form, 
            'piazza_target_url': PIAZZA_ENDPOINT,
        }, context_instance=RequestContext(request))

