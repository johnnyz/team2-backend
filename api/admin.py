from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from api.models import appUser, MeditationSession, ExerciseSession

"""
class appUserAdmin(admin.ModelAdmin):
	list_display = ('user_id_display', 'user', 'start_date', 'meditation_time', 'exercise_day_of_week',
			'exercise_time', 'created_at', 'updated_at')
	fields = ['user', 'start_date', 'meditation_time', 'exercise_day_of_week',
			'exercise_time', 'created_at', 'updated_at']
	readonly_fields = ('created_at', 'updated_at')

	def user_id_display(self, obj):
		return obj.user_id
	user_id_display.short_description = 'User ID'
"""

class MeditationSessionAdmin(admin.ModelAdmin):
	list_display = ('id', 'meditation_id', 'user_id_display', 'user', 'percent_completed', 'created_at', 'updated_at')
	fields = ['meditation_id', 'user', 'percent_completed', 'created_at', 'updated_at']
	readonly_fields = ('created_at', 'updated_at')

	def user_id_display(self, obj):
		return obj.user_id
	user_id_display.short_description = 'User ID'

class ExerciseSessionAdmin(admin.ModelAdmin):
	list_display = ('id', 'exercise_id', 'user_id_display', 'user', 'percent_completed', 'created_at', 'updated_at')
	fields = ['exercise_id', 'user', 'percent_completed', 'created_at', 'updated_at']
	readonly_fields = ('created_at', 'updated_at')

	def user_id_display(self, obj):
		return obj.user_id
	user_id_display.short_description = 'User ID'


class appUserInline(admin.StackedInline):
	model = appUser

class appUserAdmin(UserAdmin):
	inlines = [ appUserInline, ]
	list_display = ('id', 'username', 'start_date', 'meditation_time', 'exercise_day_of_week', 'exercise_time',   )

	def start_date(self, obj):
		try:
			start_date = obj.appuser.start_date
			return start_date
		except:
			return ""
	start_date.short_description = 'Start Date'

	def meditation_time(self, obj):
		try:
			meditation_time = obj.appuser.meditation_time
			return meditation_time
		except:
			return ""
	meditation_time.short_description = 'Med Time'

	def exercise_day_of_week(self, obj):
		try:
			exercise_day_of_week = obj.appuser.exercise_day_of_week
			return exercise_day_of_week
		except:
			return ""
	exercise_day_of_week.short_description = 'Exercise Day'

	def exercise_time(self, obj):
		try:
			exercise_time = obj.appuser.exercise_time
			return exercise_time
		except:
			return ""
	exercise_time.short_description = 'Exercise Time'


## Register models ##

#admin.site.register(appUser, appUserAdmin)
# Add appUser to user 
admin.site.unregister(User)
admin.site.register(User, appUserAdmin)
admin.site.register(MeditationSession, MeditationSessionAdmin)
admin.site.register(ExerciseSession, ExerciseSessionAdmin)

