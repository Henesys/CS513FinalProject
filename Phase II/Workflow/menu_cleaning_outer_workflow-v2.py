# @begin nypl_menu_cleaning_workflow @desc Overall workflow model for the menu cleaning project.
# @in menu_csv @file file:menu.csv
# @out cleaned_menu @as cleaned_menu @file file:CleanedMenu.csv
# @out open_refine_history @as open_refine_history @file file:OpenRefineHistory.json
# @out data_quality_reports @as data_quality_reports
# @out yesworkflow_model @file file:OpenFefineHistory.yw
# @out graphvis_model @file file:OpenFefineHistory.gv
# @out svg_model @file file:OpenRefineHistory.svg

    # @begin s1_profile_dataset_python @desc Python Dataset Profiling
    # @in menu_csv @as menu_csv
    # @out s1_dq_issues_python @as s1_dq_issues_python
    # @end s1_profile_dataset_python

    # @begin s1_profile_dataset_openrefine @desc OpenRefine Dataset Profiling
    # @in menu_csv @as menu_csv
    # @out s1_dq_issues_openrefine @as s1_dq_issues_openrefine
    # @end s1_profile_dataset_openrefine

    # @begin s1_combined_dq_issues @desc Combined DQ Issues
    # @in s1_dq_issues_python
    # @in s1_dq_issues_openrefine
    # @out s1_dq_issues @as s1_dq_issues
    # @end s1_profile_dataset



    # @begin s2_resolve_missing_values @desc Remove or Impute Missing Values
    # @in menu_csv @as menu_csv
    # @in s1_dq_issues_python
    # @out menu_s2_4 @as menu_s2_4 @file s2_Clean_Missing_Values.ipynb
    # @end s2_resolve_missing_values

    # @begin s2_clean_physical_description @desc Clean physical_descrption Column
    # @in menu_csv
    # @in s1_dq_issues
    # @out s2_openrefine_2 @as s2_openrefine_2 @file s2_openrefine_2.json
    # @end s2_process_physical_description

    # @begin s2_clean_location_data @desc Clean location_data Column
    # @in menu_csv
    # @in s1_dq_issues
    # @out s2_openrefine_3 @as s2_openrefine_3 @file s2_openrefine_3.json
    # @end s2_clean_location_data

    # @begin s2_standardize_event @desc Standardize event Column
    # @in menu_csv
    # @in s1_dq_issues
    # @out s2_openrefine_1 @as s2_openrefine_1 @file s2_openrefine_1.json
    # @end s2_standardize_event

    # @begin s2_merge @desc Merge Open Refine Cleaning Tasks
    # @in s2_openrefine_2
    # @in s2_openrefine_3
    # @in s2_openrefine_1
    # @out s2_combined_openrefine @as s2_combined_openrefine @file file:combined_openrefine.json
    # @end s2_merge

    # @begin s2_clean_missing_values @desc Remove or Impute Missing Values
    # @in menu_csv @as menu_csv
    # @in menu_s2_4
    # @out s2_menu_csv @as s2_menu_csv @file file:menu_data_1.csv
    # @end s2_clean_missing_values

    # @begin s2_s2_combined_openrefine_cleaning @desc Final Cleaning of Dataset
    # @in s2_menu_csv
    # @in s2_combined_openrefine
    # @out cleaned_menu @as cleaned_menu @file file:CleanedMenu.csv
    # @out open_refine_history @as open_refine_history @file file:OpenRefineHistory.json
    # @end s2_s2_combined_openrefine_cleaning

    # @begin inner_workflow_documentation @desc Document Inner Workflow
    # @in open_refine_history
    # @out yesworkflow_model @file file:OpenFefineHistory.yw
    # @out graphvis_model @file file:OpenFefineHistory.gv
    # @out svg_model @file file:OpenRefineHistory.svg
    # @end inner_workflow_documentation

    # @begin s3_data_quality_check @desc Data Quality Check
    # @in menu_csv
    # @in cleaned_menu
    # @out data_quality_reports
    # @end s3_data_quality_check

    
# @end CS512_Phase_II