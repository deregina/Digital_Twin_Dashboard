from django.contrib import admin
from .models import project, location, weather, soil_profile, experement, uav_data, satellite_data, forecasted_data_uav, forecasted_data_satellite
from import_export.admin import ImportExportModelAdmin

# header in admin area 
admin.site.site_header = 'Digital Twin Dashboard'

# adding tabels to admin area
@admin.register(project)
class ProjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'project_id', 'user_id', 
        'project_editors', 'start_year', 'acesss',
        'crop','funding_source', 'metadata'
    )

@admin.register(location)
class ProjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'location_id','year_added','plot_boundary','fid','state_id','county_id',
        'latitude','longitude','contact_info','metadata'
    )

@admin.register(weather)
class ProjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'weather_id', 'location_id'
    )

@admin.register(soil_profile)
class ProjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'soil_id', 'location_id'
    )


@admin.register(experement)
class ProjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'experement_id','project_id','location_id','year','planting_date',
        'pix_source_1','pix_rate_1','pix_timing_1','pix_unit_1','pix_source_2','pix_rate_2','pix_timing_2','pix_unit_2','pix_source_3','pix_rate_3',
        'pix_timing_3','pix_unit_3','n_source_1','n_timing_1','n_rate_1','n_unit_1','n_source_2','n_timing_2','n_rate_2','n_unit_2','n_source_3',
        'n_timing_3','n_rate_3', 'n_unit_3','defoliation_source_1','defoliation_timing_1','defoliation_rate_1','defoliation_unit_1',
        'defoliation_source_2','defoliation_timing_2','defoliation_rate_2','defoliation_unit_2','defoliation_source_3','defoliation_timing_3',
        'defoliation_rate_3','defoliation_unit_3','uav_raw','satellite_raw','uav_orthomosiac_RGB','uav_orthomosiac_MS','uav_dsm','metadata'
    )

@admin.register(uav_data)
class ProjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'experiment_id','fid','feature','emergence_data', 'Yield',
        'd_1_1','d_1_2','d_1_3','d_1_4','d_1_5','d_1_6','d_1_7','d_1_8','d_1_9','d_1_10','d_1_11','d_1_12','d_1_13','d_1_14',
        'd_1_15','d_1_16','d_1_17','d_1_18','d_1_19','d_1_20','d_1_21','d_1_22','d_1_23','d_1_24','d_1_25','d_1_26','d_1_27',
        'd_1_28','d_1_29','d_1_30','d_1_31','d_2_1','d_2_2','d_2_3','d_2_4','d_2_5','d_2_6','d_2_7','d_2_8','d_2_9','d_2_10',
        'd_2_11','d_2_12','d_2_13','d_2_14','d_2_15','d_2_16','d_2_17','d_2_18','d_2_19','d_2_20','d_2_21','d_2_22','d_2_23',
        'd_2_24','d_2_25','d_2_26','d_2_27','d_2_28','d_2_29','d_3_1','d_3_2','d_3_3','d_3_4','d_3_5','d_3_6','d_3_7','d_3_8',
        'd_3_9','d_3_10','d_3_11','d_3_12','d_3_13','d_3_14','d_3_15','d_3_16','d_3_17','d_3_18','d_3_19','d_3_20','d_3_21',
        'd_3_22','d_3_23','d_3_24','d_3_25','d_3_26','d_3_27','d_3_28','d_3_29','d_3_30','d_3_31','d_4_1','d_4_2','d_4_3','d_4_4',
        'd_4_5','d_4_6','d_4_7','d_4_8','d_4_9','d_4_10','d_4_11','d_4_12','d_4_13','d_4_14','d_4_15','d_4_16','d_4_17','d_4_18',
        'd_4_19','d_4_20','d_4_21','d_4_22','d_4_23','d_4_24','d_4_25','d_4_26','d_4_27','d_4_28','d_4_29','d_4_30','d_5_1',
        'd_5_2','d_5_3','d_5_4','d_5_5','d_5_6','d_5_7','d_5_8','d_5_9','d_5_10','d_5_11','d_5_12','d_5_13','d_5_14','d_5_15',
        'd_5_16','d_5_17','d_5_18','d_5_19','d_5_20','d_5_21','d_5_22','d_5_23','d_5_24','d_5_25','d_5_26','d_5_27','d_5_28',
        'd_5_29','d_5_30','d_5_31','d_6_1','d_6_2','d_6_3','d_6_4','d_6_5','d_6_6','d_6_7','d_6_8','d_6_9','d_6_10','d_6_11',
        'd_6_12','d_6_13','d_6_14','d_6_15','d_6_16','d_6_17','d_6_18','d_6_19','d_6_20','d_6_21','d_6_22','d_6_23','d_6_24',
        'd_6_25','d_6_26','d_6_27','d_6_28','d_6_29','d_6_30','d_7_1','d_7_2','d_7_3','d_7_4','d_7_5','d_7_6','d_7_7','d_7_8',
        'd_7_9','d_7_10','d_7_11','d_7_12','d_7_13','d_7_14','d_7_15','d_7_16','d_7_17','d_7_18','d_7_19','d_7_20','d_7_21',
        'd_7_22','d_7_23','d_7_24','d_7_25','d_7_26','d_7_27','d_7_28','d_7_29','d_7_30','d_7_31','d_8_1','d_8_2','d_8_3',
        'd_8_4','d_8_5','d_8_6','d_8_7','d_8_8','d_8_9','d_8_10','d_8_11','d_8_12','d_8_13','d_8_14','d_8_15','d_8_16',
        'd_8_17','d_8_18','d_8_19','d_8_20','d_8_21','d_8_22','d_8_23','d_8_24','d_8_25','d_8_26','d_8_27','d_8_28',
        'd_8_29','d_8_30','d_8_31','d_9_1','d_9_2','d_9_3','d_9_4','d_9_5','d_9_6','d_9_7','d_9_8','d_9_9','d_9_10',
        'd_9_11','d_9_12','d_9_13','d_9_14','d_9_15','d_9_16','d_9_17','d_9_18','d_9_19','d_9_20','d_9_21','d_9_22',
        'd_9_23','d_9_24','d_9_25','d_9_26','d_9_27','d_9_28','d_9_29','d_9_30','d_10_1','d_10_2','d_10_3','d_10_4',
        'd_10_5','d_10_6','d_10_7','d_10_8','d_10_9','d_10_10','d_10_11','d_10_12','d_10_13','d_10_14','d_10_15',
        'd_10_16','d_10_17','d_10_18','d_10_19','d_10_20','d_10_21','d_10_22','d_10_23','d_10_24','d_10_25','d_10_26',
        'd_10_27','d_10_28','d_10_29','d_10_30','d_10_31','d_11_1','d_11_2','d_11_3','d_11_4','d_11_5','d_11_6','d_11_7',
        'd_11_8','d_11_9','d_11_10','d_11_11','d_11_12','d_11_13','d_11_14','d_11_15','d_11_16','d_11_17','d_11_18','d_11_19',
        'd_11_20','d_11_21','d_11_22','d_11_23','d_11_24','d_11_25','d_11_26','d_11_27','d_11_28','d_11_29','d_11_30',
        'd_12_1','d_12_2','d_12_3','d_12_4','d_12_5','d_12_6','d_12_7','d_12_8','d_12_9','d_12_10','d_12_11','d_12_12',
        'd_12_13','d_12_14','d_12_15','d_12_16','d_12_17','d_12_18','d_12_19','d_12_20','d_12_21','d_12_22','d_12_23',
        'd_12_24','d_12_25','d_12_26','d_12_27','d_12_28','d_12_29','d_12_30','d_12_31'
    )

@admin.register(satellite_data)
class ProjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'experiment_id','fid','feature','emergence_data',
        'd_1_1','d_1_2','d_1_3','d_1_4','d_1_5','d_1_6','d_1_7','d_1_8','d_1_9','d_1_10','d_1_11','d_1_12','d_1_13','d_1_14',
        'd_1_15','d_1_16','d_1_17','d_1_18','d_1_19','d_1_20','d_1_21','d_1_22','d_1_23','d_1_24','d_1_25','d_1_26','d_1_27',
        'd_1_28','d_1_29','d_1_30','d_1_31','d_2_1','d_2_2','d_2_3','d_2_4','d_2_5','d_2_6','d_2_7','d_2_8','d_2_9','d_2_10',
        'd_2_11','d_2_12','d_2_13','d_2_14','d_2_15','d_2_16','d_2_17','d_2_18','d_2_19','d_2_20','d_2_21','d_2_22','d_2_23',
        'd_2_24','d_2_25','d_2_26','d_2_27','d_2_28','d_2_29','d_3_1','d_3_2','d_3_3','d_3_4','d_3_5','d_3_6','d_3_7','d_3_8',
        'd_3_9','d_3_10','d_3_11','d_3_12','d_3_13','d_3_14','d_3_15','d_3_16','d_3_17','d_3_18','d_3_19','d_3_20','d_3_21',
        'd_3_22','d_3_23','d_3_24','d_3_25','d_3_26','d_3_27','d_3_28','d_3_29','d_3_30','d_3_31','d_4_1','d_4_2','d_4_3','d_4_4',
        'd_4_5','d_4_6','d_4_7','d_4_8','d_4_9','d_4_10','d_4_11','d_4_12','d_4_13','d_4_14','d_4_15','d_4_16','d_4_17','d_4_18',
        'd_4_19','d_4_20','d_4_21','d_4_22','d_4_23','d_4_24','d_4_25','d_4_26','d_4_27','d_4_28','d_4_29','d_4_30','d_5_1',
        'd_5_2','d_5_3','d_5_4','d_5_5','d_5_6','d_5_7','d_5_8','d_5_9','d_5_10','d_5_11','d_5_12','d_5_13','d_5_14','d_5_15',
        'd_5_16','d_5_17','d_5_18','d_5_19','d_5_20','d_5_21','d_5_22','d_5_23','d_5_24','d_5_25','d_5_26','d_5_27','d_5_28',
        'd_5_29','d_5_30','d_5_31','d_6_1','d_6_2','d_6_3','d_6_4','d_6_5','d_6_6','d_6_7','d_6_8','d_6_9','d_6_10','d_6_11',
        'd_6_12','d_6_13','d_6_14','d_6_15','d_6_16','d_6_17','d_6_18','d_6_19','d_6_20','d_6_21','d_6_22','d_6_23','d_6_24',
        'd_6_25','d_6_26','d_6_27','d_6_28','d_6_29','d_6_30','d_7_1','d_7_2','d_7_3','d_7_4','d_7_5','d_7_6','d_7_7','d_7_8',
        'd_7_9','d_7_10','d_7_11','d_7_12','d_7_13','d_7_14','d_7_15','d_7_16','d_7_17','d_7_18','d_7_19','d_7_20','d_7_21',
        'd_7_22','d_7_23','d_7_24','d_7_25','d_7_26','d_7_27','d_7_28','d_7_29','d_7_30','d_7_31','d_8_1','d_8_2','d_8_3',
        'd_8_4','d_8_5','d_8_6','d_8_7','d_8_8','d_8_9','d_8_10','d_8_11','d_8_12','d_8_13','d_8_14','d_8_15','d_8_16',
        'd_8_17','d_8_18','d_8_19','d_8_20','d_8_21','d_8_22','d_8_23','d_8_24','d_8_25','d_8_26','d_8_27','d_8_28',
        'd_8_29','d_8_30','d_8_31','d_9_1','d_9_2','d_9_3','d_9_4','d_9_5','d_9_6','d_9_7','d_9_8','d_9_9','d_9_10',
        'd_9_11','d_9_12','d_9_13','d_9_14','d_9_15','d_9_16','d_9_17','d_9_18','d_9_19','d_9_20','d_9_21','d_9_22',
        'd_9_23','d_9_24','d_9_25','d_9_26','d_9_27','d_9_28','d_9_29','d_9_30','d_10_1','d_10_2','d_10_3','d_10_4',
        'd_10_5','d_10_6','d_10_7','d_10_8','d_10_9','d_10_10','d_10_11','d_10_12','d_10_13','d_10_14','d_10_15',
        'd_10_16','d_10_17','d_10_18','d_10_19','d_10_20','d_10_21','d_10_22','d_10_23','d_10_24','d_10_25','d_10_26',
        'd_10_27','d_10_28','d_10_29','d_10_30','d_10_31','d_11_1','d_11_2','d_11_3','d_11_4','d_11_5','d_11_6','d_11_7',
        'd_11_8','d_11_9','d_11_10','d_11_11','d_11_12','d_11_13','d_11_14','d_11_15','d_11_16','d_11_17','d_11_18','d_11_19',
        'd_11_20','d_11_21','d_11_22','d_11_23','d_11_24','d_11_25','d_11_26','d_11_27','d_11_28','d_11_29','d_11_30',
        'd_12_1','d_12_2','d_12_3','d_12_4','d_12_5','d_12_6','d_12_7','d_12_8','d_12_9','d_12_10','d_12_11','d_12_12',
        'd_12_13','d_12_14','d_12_15','d_12_16','d_12_17','d_12_18','d_12_19','d_12_20','d_12_21','d_12_22','d_12_23',
        'd_12_24','d_12_25','d_12_26','d_12_27','d_12_28','d_12_29','d_12_30','d_12_31'
    )


@admin.register(forecasted_data_uav)
class ProjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'experiment_id','fid','feature','emergence_data', 'forecasting_date', 'pridicted_yield',
        'd_1_1','d_1_2','d_1_3','d_1_4','d_1_5','d_1_6','d_1_7','d_1_8','d_1_9','d_1_10','d_1_11','d_1_12','d_1_13','d_1_14',
        'd_1_15','d_1_16','d_1_17','d_1_18','d_1_19','d_1_20','d_1_21','d_1_22','d_1_23','d_1_24','d_1_25','d_1_26','d_1_27',
        'd_1_28','d_1_29','d_1_30','d_1_31','d_2_1','d_2_2','d_2_3','d_2_4','d_2_5','d_2_6','d_2_7','d_2_8','d_2_9','d_2_10',
        'd_2_11','d_2_12','d_2_13','d_2_14','d_2_15','d_2_16','d_2_17','d_2_18','d_2_19','d_2_20','d_2_21','d_2_22','d_2_23',
        'd_2_24','d_2_25','d_2_26','d_2_27','d_2_28','d_2_29','d_3_1','d_3_2','d_3_3','d_3_4','d_3_5','d_3_6','d_3_7','d_3_8',
        'd_3_9','d_3_10','d_3_11','d_3_12','d_3_13','d_3_14','d_3_15','d_3_16','d_3_17','d_3_18','d_3_19','d_3_20','d_3_21',
        'd_3_22','d_3_23','d_3_24','d_3_25','d_3_26','d_3_27','d_3_28','d_3_29','d_3_30','d_3_31','d_4_1','d_4_2','d_4_3','d_4_4',
        'd_4_5','d_4_6','d_4_7','d_4_8','d_4_9','d_4_10','d_4_11','d_4_12','d_4_13','d_4_14','d_4_15','d_4_16','d_4_17','d_4_18',
        'd_4_19','d_4_20','d_4_21','d_4_22','d_4_23','d_4_24','d_4_25','d_4_26','d_4_27','d_4_28','d_4_29','d_4_30','d_5_1',
        'd_5_2','d_5_3','d_5_4','d_5_5','d_5_6','d_5_7','d_5_8','d_5_9','d_5_10','d_5_11','d_5_12','d_5_13','d_5_14','d_5_15',
        'd_5_16','d_5_17','d_5_18','d_5_19','d_5_20','d_5_21','d_5_22','d_5_23','d_5_24','d_5_25','d_5_26','d_5_27','d_5_28',
        'd_5_29','d_5_30','d_5_31','d_6_1','d_6_2','d_6_3','d_6_4','d_6_5','d_6_6','d_6_7','d_6_8','d_6_9','d_6_10','d_6_11',
        'd_6_12','d_6_13','d_6_14','d_6_15','d_6_16','d_6_17','d_6_18','d_6_19','d_6_20','d_6_21','d_6_22','d_6_23','d_6_24',
        'd_6_25','d_6_26','d_6_27','d_6_28','d_6_29','d_6_30','d_7_1','d_7_2','d_7_3','d_7_4','d_7_5','d_7_6','d_7_7','d_7_8',
        'd_7_9','d_7_10','d_7_11','d_7_12','d_7_13','d_7_14','d_7_15','d_7_16','d_7_17','d_7_18','d_7_19','d_7_20','d_7_21',
        'd_7_22','d_7_23','d_7_24','d_7_25','d_7_26','d_7_27','d_7_28','d_7_29','d_7_30','d_7_31','d_8_1','d_8_2','d_8_3',
        'd_8_4','d_8_5','d_8_6','d_8_7','d_8_8','d_8_9','d_8_10','d_8_11','d_8_12','d_8_13','d_8_14','d_8_15','d_8_16',
        'd_8_17','d_8_18','d_8_19','d_8_20','d_8_21','d_8_22','d_8_23','d_8_24','d_8_25','d_8_26','d_8_27','d_8_28',
        'd_8_29','d_8_30','d_8_31','d_9_1','d_9_2','d_9_3','d_9_4','d_9_5','d_9_6','d_9_7','d_9_8','d_9_9','d_9_10',
        'd_9_11','d_9_12','d_9_13','d_9_14','d_9_15','d_9_16','d_9_17','d_9_18','d_9_19','d_9_20','d_9_21','d_9_22',
        'd_9_23','d_9_24','d_9_25','d_9_26','d_9_27','d_9_28','d_9_29','d_9_30','d_10_1','d_10_2','d_10_3','d_10_4',
        'd_10_5','d_10_6','d_10_7','d_10_8','d_10_9','d_10_10','d_10_11','d_10_12','d_10_13','d_10_14','d_10_15',
        'd_10_16','d_10_17','d_10_18','d_10_19','d_10_20','d_10_21','d_10_22','d_10_23','d_10_24','d_10_25','d_10_26',
        'd_10_27','d_10_28','d_10_29','d_10_30','d_10_31','d_11_1','d_11_2','d_11_3','d_11_4','d_11_5','d_11_6','d_11_7',
        'd_11_8','d_11_9','d_11_10','d_11_11','d_11_12','d_11_13','d_11_14','d_11_15','d_11_16','d_11_17','d_11_18','d_11_19',
        'd_11_20','d_11_21','d_11_22','d_11_23','d_11_24','d_11_25','d_11_26','d_11_27','d_11_28','d_11_29','d_11_30',
        'd_12_1','d_12_2','d_12_3','d_12_4','d_12_5','d_12_6','d_12_7','d_12_8','d_12_9','d_12_10','d_12_11','d_12_12',
        'd_12_13','d_12_14','d_12_15','d_12_16','d_12_17','d_12_18','d_12_19','d_12_20','d_12_21','d_12_22','d_12_23',
        'd_12_24','d_12_25','d_12_26','d_12_27','d_12_28','d_12_29','d_12_30','d_12_31'
    )

@admin.register(forecasted_data_satellite)
class ProjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'experiment_id','fid','feature','emergence_data', 'forecasting_date', 'pridicted_yield',
        'd_1_1','d_1_2','d_1_3','d_1_4','d_1_5','d_1_6','d_1_7','d_1_8','d_1_9','d_1_10','d_1_11','d_1_12','d_1_13','d_1_14',
        'd_1_15','d_1_16','d_1_17','d_1_18','d_1_19','d_1_20','d_1_21','d_1_22','d_1_23','d_1_24','d_1_25','d_1_26','d_1_27',
        'd_1_28','d_1_29','d_1_30','d_1_31','d_2_1','d_2_2','d_2_3','d_2_4','d_2_5','d_2_6','d_2_7','d_2_8','d_2_9','d_2_10',
        'd_2_11','d_2_12','d_2_13','d_2_14','d_2_15','d_2_16','d_2_17','d_2_18','d_2_19','d_2_20','d_2_21','d_2_22','d_2_23',
        'd_2_24','d_2_25','d_2_26','d_2_27','d_2_28','d_2_29','d_3_1','d_3_2','d_3_3','d_3_4','d_3_5','d_3_6','d_3_7','d_3_8',
        'd_3_9','d_3_10','d_3_11','d_3_12','d_3_13','d_3_14','d_3_15','d_3_16','d_3_17','d_3_18','d_3_19','d_3_20','d_3_21',
        'd_3_22','d_3_23','d_3_24','d_3_25','d_3_26','d_3_27','d_3_28','d_3_29','d_3_30','d_3_31','d_4_1','d_4_2','d_4_3','d_4_4',
        'd_4_5','d_4_6','d_4_7','d_4_8','d_4_9','d_4_10','d_4_11','d_4_12','d_4_13','d_4_14','d_4_15','d_4_16','d_4_17','d_4_18',
        'd_4_19','d_4_20','d_4_21','d_4_22','d_4_23','d_4_24','d_4_25','d_4_26','d_4_27','d_4_28','d_4_29','d_4_30','d_5_1',
        'd_5_2','d_5_3','d_5_4','d_5_5','d_5_6','d_5_7','d_5_8','d_5_9','d_5_10','d_5_11','d_5_12','d_5_13','d_5_14','d_5_15',
        'd_5_16','d_5_17','d_5_18','d_5_19','d_5_20','d_5_21','d_5_22','d_5_23','d_5_24','d_5_25','d_5_26','d_5_27','d_5_28',
        'd_5_29','d_5_30','d_5_31','d_6_1','d_6_2','d_6_3','d_6_4','d_6_5','d_6_6','d_6_7','d_6_8','d_6_9','d_6_10','d_6_11',
        'd_6_12','d_6_13','d_6_14','d_6_15','d_6_16','d_6_17','d_6_18','d_6_19','d_6_20','d_6_21','d_6_22','d_6_23','d_6_24',
        'd_6_25','d_6_26','d_6_27','d_6_28','d_6_29','d_6_30','d_7_1','d_7_2','d_7_3','d_7_4','d_7_5','d_7_6','d_7_7','d_7_8',
        'd_7_9','d_7_10','d_7_11','d_7_12','d_7_13','d_7_14','d_7_15','d_7_16','d_7_17','d_7_18','d_7_19','d_7_20','d_7_21',
        'd_7_22','d_7_23','d_7_24','d_7_25','d_7_26','d_7_27','d_7_28','d_7_29','d_7_30','d_7_31','d_8_1','d_8_2','d_8_3',
        'd_8_4','d_8_5','d_8_6','d_8_7','d_8_8','d_8_9','d_8_10','d_8_11','d_8_12','d_8_13','d_8_14','d_8_15','d_8_16',
        'd_8_17','d_8_18','d_8_19','d_8_20','d_8_21','d_8_22','d_8_23','d_8_24','d_8_25','d_8_26','d_8_27','d_8_28',
        'd_8_29','d_8_30','d_8_31','d_9_1','d_9_2','d_9_3','d_9_4','d_9_5','d_9_6','d_9_7','d_9_8','d_9_9','d_9_10',
        'd_9_11','d_9_12','d_9_13','d_9_14','d_9_15','d_9_16','d_9_17','d_9_18','d_9_19','d_9_20','d_9_21','d_9_22',
        'd_9_23','d_9_24','d_9_25','d_9_26','d_9_27','d_9_28','d_9_29','d_9_30','d_10_1','d_10_2','d_10_3','d_10_4',
        'd_10_5','d_10_6','d_10_7','d_10_8','d_10_9','d_10_10','d_10_11','d_10_12','d_10_13','d_10_14','d_10_15',
        'd_10_16','d_10_17','d_10_18','d_10_19','d_10_20','d_10_21','d_10_22','d_10_23','d_10_24','d_10_25','d_10_26',
        'd_10_27','d_10_28','d_10_29','d_10_30','d_10_31','d_11_1','d_11_2','d_11_3','d_11_4','d_11_5','d_11_6','d_11_7',
        'd_11_8','d_11_9','d_11_10','d_11_11','d_11_12','d_11_13','d_11_14','d_11_15','d_11_16','d_11_17','d_11_18','d_11_19',
        'd_11_20','d_11_21','d_11_22','d_11_23','d_11_24','d_11_25','d_11_26','d_11_27','d_11_28','d_11_29','d_11_30',
        'd_12_1','d_12_2','d_12_3','d_12_4','d_12_5','d_12_6','d_12_7','d_12_8','d_12_9','d_12_10','d_12_11','d_12_12',
        'd_12_13','d_12_14','d_12_15','d_12_16','d_12_17','d_12_18','d_12_19','d_12_20','d_12_21','d_12_22','d_12_23',
        'd_12_24','d_12_25','d_12_26','d_12_27','d_12_28','d_12_29','d_12_30','d_12_31'
    )