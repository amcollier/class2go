# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Institution'
        db.create_table(u'c2g_institutions', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('country', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('city', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('domains', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('c2g', ['Institution'])

        # Adding model 'Course'
        db.create_table(u'c2g_courses', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('mode', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['c2g.Course'])),
            ('live_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('is_deleted', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('institution', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['c2g.Institution'], null=True)),
            ('student_group', self.gf('django.db.models.fields.related.ForeignKey')(related_name='student_group', to=orm['auth.Group'])),
            ('instructor_group', self.gf('django.db.models.fields.related.ForeignKey')(related_name='instructor_group', to=orm['auth.Group'])),
            ('tas_group', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tas_group', to=orm['auth.Group'])),
            ('readonly_tas_group', self.gf('django.db.models.fields.related.ForeignKey')(related_name='readonly_tas_group', to=orm['auth.Group'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('syllabus', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('term', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('calendar_start', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('calendar_end', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('list_publicly', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('handle', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, db_index=True)),
        ))
        db.send_create_signal('c2g', ['Course'])

        # Adding model 'ContentSection'
        db.create_table(u'c2g_content_sections', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('mode', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['c2g.ContentSection'])),
            ('live_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('index', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('is_deleted', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['c2g.Course'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('c2g', ['ContentSection'])

        # Adding model 'AdditionalPage'
        db.create_table(u'c2g_additional_pages', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('mode', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['c2g.AdditionalPage'])),
            ('live_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('index', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('is_deleted', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['c2g.Course'])),
            ('menu_slug', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['c2g.ContentSection'], null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('c2g', ['AdditionalPage'])

        # Adding model 'File'
        db.create_table(u'c2g_files', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('mode', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['c2g.File'])),
            ('live_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('index', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('is_deleted', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['c2g.Course'])),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['c2g.ContentSection'], null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('handle', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, db_index=True)),
        ))
        db.send_create_signal('c2g', ['File'])

        # Adding model 'Announcement'
        db.create_table(u'c2g_announcements', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('mode', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['c2g.Announcement'])),
            ('live_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('index', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('is_deleted', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['c2g.Course'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('c2g', ['Announcement'])

        # Adding model 'StudentSection'
        db.create_table(u'c2g_sections', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('is_deleted', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['c2g.Course'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('capacity', self.gf('django.db.models.fields.IntegerField')(default=999)),
        ))
        db.send_create_signal('c2g', ['StudentSection'])

        # Adding M2M table for field members on 'StudentSection'
        db.create_table(u'c2g_sections_members', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('studentsection', models.ForeignKey(orm['c2g.studentsection'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique(u'c2g_sections_members', ['studentsection_id', 'user_id'])

        # Adding model 'UserProfile'
        db.create_table(u'c2g_user_profiles', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('site_data', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('c2g', ['UserProfile'])

        # Adding model 'Video'
        db.create_table(u'c2g_videos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('mode', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['c2g.Video'])),
            ('live_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('index', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('is_deleted', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['c2g.Course'])),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['c2g.ContentSection'], null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(default='youtube', max_length=30)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('duration', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, null=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('handle', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, db_index=True)),
        ))
        db.send_create_signal('c2g', ['Video'])

        # Adding model 'VideoActivity'
        db.create_table(u'c2g_video_activity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['c2g.Course'])),
            ('video', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['c2g.Video'])),
            ('start_seconds', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal('c2g', ['VideoActivity'])

        # Adding model 'ProblemSet'
        db.create_table(u'c2g_problem_sets', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('mode', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['c2g.ProblemSet'])),
            ('live_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('index', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('is_deleted', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['c2g.Course'])),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['c2g.ContentSection'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('due_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('grace_period', self.gf('django.db.models.fields.DateTimeField')()),
            ('partial_credit_deadline', self.gf('django.db.models.fields.DateTimeField')()),
            ('assessment_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('late_penalty', self.gf('django.db.models.fields.IntegerField')()),
            ('submissions_permitted', self.gf('django.db.models.fields.IntegerField')()),
            ('resubmission_penalty', self.gf('django.db.models.fields.IntegerField')()),
            ('randomize', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('c2g', ['ProblemSet'])

        # Adding model 'Exercise'
        db.create_table(u'c2g_exercises', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('is_deleted', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('fileName', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True)),
            ('handle', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, db_index=True)),
        ))
        db.send_create_signal('c2g', ['Exercise'])

        # Adding model 'ProblemSetToExercise'
        db.create_table(u'c2g_problemset_to_exercise', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('problemSet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['c2g.ProblemSet'])),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['c2g.Exercise'])),
            ('number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['c2g.ProblemSetToExercise'], null=True, blank=True)),
            ('mode', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('c2g', ['ProblemSetToExercise'])

        # Adding model 'VideoToExercise'
        db.create_table(u'c2g_video_to_exercise', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('video', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['c2g.Video'])),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['c2g.Exercise'])),
            ('video_time', self.gf('django.db.models.fields.IntegerField')()),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['c2g.VideoToExercise'], null=True, blank=True)),
            ('mode', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('c2g', ['VideoToExercise'])

        # Adding model 'ProblemActivity'
        db.create_table(u'c2g_problem_activity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('video_to_exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['c2g.VideoToExercise'], null=True)),
            ('problemset_to_exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['c2g.ProblemSetToExercise'], null=True)),
            ('problem_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('complete', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('attempt_content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('count_hints', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('time_taken', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('attempt_number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sha1', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('seed', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('problem_type', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('review_mode', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('topic_mode', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('casing', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('card', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('cards_done', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cards_left', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('user_selection_val', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True)),
            ('user_choices', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True)),
        ))
        db.send_create_signal('c2g', ['ProblemActivity'])

        # Adding model 'NewsEvent'
        db.create_table(u'c2g_news_events', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['c2g.Course'])),
            ('event', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('c2g', ['NewsEvent'])


    def backwards(self, orm):
        # Deleting model 'Institution'
        db.delete_table(u'c2g_institutions')

        # Deleting model 'Course'
        db.delete_table(u'c2g_courses')

        # Deleting model 'ContentSection'
        db.delete_table(u'c2g_content_sections')

        # Deleting model 'AdditionalPage'
        db.delete_table(u'c2g_additional_pages')

        # Deleting model 'File'
        db.delete_table(u'c2g_files')

        # Deleting model 'Announcement'
        db.delete_table(u'c2g_announcements')

        # Deleting model 'StudentSection'
        db.delete_table(u'c2g_sections')

        # Removing M2M table for field members on 'StudentSection'
        db.delete_table('c2g_sections_members')

        # Deleting model 'UserProfile'
        db.delete_table(u'c2g_user_profiles')

        # Deleting model 'Video'
        db.delete_table(u'c2g_videos')

        # Deleting model 'VideoActivity'
        db.delete_table(u'c2g_video_activity')

        # Deleting model 'ProblemSet'
        db.delete_table(u'c2g_problem_sets')

        # Deleting model 'Exercise'
        db.delete_table(u'c2g_exercises')

        # Deleting model 'ProblemSetToExercise'
        db.delete_table(u'c2g_problemset_to_exercise')

        # Deleting model 'VideoToExercise'
        db.delete_table(u'c2g_video_to_exercise')

        # Deleting model 'ProblemActivity'
        db.delete_table(u'c2g_problem_activity')

        # Deleting model 'NewsEvent'
        db.delete_table(u'c2g_news_events')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'c2g.additionalpage': {
            'Meta': {'object_name': 'AdditionalPage', 'db_table': "u'c2g_additional_pages'"},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['c2g.Course']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': "orm['c2g.AdditionalPage']"}),
            'index': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'live_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'menu_slug': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mode': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['c2g.ContentSection']", 'null': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'c2g.announcement': {
            'Meta': {'object_name': 'Announcement', 'db_table': "u'c2g_announcements'"},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['c2g.Course']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': "orm['c2g.Announcement']"}),
            'index': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'live_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'mode': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'c2g.contentsection': {
            'Meta': {'object_name': 'ContentSection', 'db_table': "u'c2g_content_sections'"},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['c2g.Course']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': "orm['c2g.ContentSection']"}),
            'index': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'live_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'mode': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'c2g.course': {
            'Meta': {'object_name': 'Course', 'db_table': "u'c2g_courses'"},
            'calendar_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'calendar_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'handle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': "orm['c2g.Course']"}),
            'institution': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['c2g.Institution']", 'null': 'True'}),
            'instructor_group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'instructor_group'", 'to': "orm['auth.Group']"}),
            'is_deleted': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'list_publicly': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'live_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'mode': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'readonly_tas_group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'readonly_tas_group'", 'to': "orm['auth.Group']"}),
            'student_group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'student_group'", 'to': "orm['auth.Group']"}),
            'syllabus': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'tas_group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tas_group'", 'to': "orm['auth.Group']"}),
            'term': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'c2g.exercise': {
            'Meta': {'object_name': 'Exercise', 'db_table': "u'c2g_exercises'"},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'fileName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'handle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'problemSet': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['c2g.ProblemSet']", 'through': "orm['c2g.ProblemSetToExercise']", 'symmetrical': 'False'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'video': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['c2g.Video']", 'through': "orm['c2g.VideoToExercise']", 'symmetrical': 'False'})
        },
        'c2g.file': {
            'Meta': {'object_name': 'File', 'db_table': "u'c2g_files'"},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['c2g.Course']"}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'handle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': "orm['c2g.File']"}),
            'index': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'live_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'mode': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['c2g.ContentSection']", 'null': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'c2g.institution': {
            'Meta': {'object_name': 'Institution', 'db_table': "u'c2g_institutions'"},
            'city': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'country': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'domains': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        'c2g.newsevent': {
            'Meta': {'object_name': 'NewsEvent', 'db_table': "u'c2g_news_events'"},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['c2g.Course']"}),
            'event': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'c2g.problemactivity': {
            'Meta': {'object_name': 'ProblemActivity', 'db_table': "u'c2g_problem_activity'"},
            'attempt_content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'attempt_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'card': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cards_done': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cards_left': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'casing': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'complete': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'count_hints': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'problem_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'problem_type': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'problemset_to_exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['c2g.ProblemSetToExercise']", 'null': 'True'}),
            'review_mode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'seed': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sha1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'time_taken': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'topic_mode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'user_choices': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'user_selection_val': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'video_to_exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['c2g.VideoToExercise']", 'null': 'True'})
        },
        'c2g.problemset': {
            'Meta': {'object_name': 'ProblemSet', 'db_table': "u'c2g_problem_sets'"},
            'assessment_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['c2g.Course']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'due_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'grace_period': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': "orm['c2g.ProblemSet']"}),
            'index': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'late_penalty': ('django.db.models.fields.IntegerField', [], {}),
            'live_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'mode': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'partial_credit_deadline': ('django.db.models.fields.DateTimeField', [], {}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'randomize': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'resubmission_penalty': ('django.db.models.fields.IntegerField', [], {}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['c2g.ContentSection']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'submissions_permitted': ('django.db.models.fields.IntegerField', [], {}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'c2g.problemsettoexercise': {
            'Meta': {'object_name': 'ProblemSetToExercise', 'db_table': "u'c2g_problemset_to_exercise'"},
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['c2g.Exercise']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['c2g.ProblemSetToExercise']", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mode': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'problemSet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['c2g.ProblemSet']"})
        },
        'c2g.studentsection': {
            'Meta': {'object_name': 'StudentSection', 'db_table': "u'c2g_sections'"},
            'capacity': ('django.db.models.fields.IntegerField', [], {'default': '999'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['c2g.Course']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'c2g.userprofile': {
            'Meta': {'object_name': 'UserProfile', 'db_table': "u'c2g_user_profiles'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site_data': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'c2g.video': {
            'Meta': {'object_name': 'Video', 'db_table': "u'c2g_videos'"},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['c2g.Course']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'duration': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'handle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': "orm['c2g.Video']"}),
            'index': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'live_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'mode': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['c2g.ContentSection']", 'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'null': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'youtube'", 'max_length': '30'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        'c2g.videoactivity': {
            'Meta': {'object_name': 'VideoActivity', 'db_table': "u'c2g_video_activity'"},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['c2g.Course']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_seconds': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['c2g.Video']"})
        },
        'c2g.videotoexercise': {
            'Meta': {'object_name': 'VideoToExercise', 'db_table': "u'c2g_video_to_exercise'"},
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['c2g.Exercise']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['c2g.VideoToExercise']", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mode': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['c2g.Video']"}),
            'video_time': ('django.db.models.fields.IntegerField', [], {})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['c2g']