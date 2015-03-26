from django.contrib import admin

from api.models import appUser, MeditationSession, ExcerciseSession



class appUserAdmin(admin.ModelAdmin):
	user_id = user.id
	list_display = ('user', 'user_id' 'start_date', 'mediation_time', 'excercise_day_of_week',
			'excercise_time', 'created_at', 'updated_at')
	fields = ['user', 'start_date', 'mediation_time', 'excercise_day_of_week',
			'excercise_time', 'created_at', 'updated_at']
	readonly_fields = ('created_at', 'updated_at')

class MeditationSessionAdmin(admin.ModelAdmin):
	list_display = ('meditation_id', 'user', 'percent_completed', 'created_at', 'updated_at')
	fields = ['meditation_id', 'user', 'percent_completed', 'created_at', 'updated_at']
	readonly_fields = ('created_at', 'updated_at')

class ExerciseSessionAdmin(admin.ModelAdmin):
	list_display = ('excercise_id', 'user', 'percent_completed', 'created_at', 'updated_at')
	fields = ['excercise_id', 'user', 'percent_completed', 'created_at', 'updated_at']
	readonly_fields = ('created_at', 'updated_at')


# Register your models here.
admin.site.register(appUser, appUserAdmin)
admin.site.register(MeditationSession, MeditationSessionAdmin)
admin.site.register(ExcerciseSession, ExerciseSessionAdmin)

