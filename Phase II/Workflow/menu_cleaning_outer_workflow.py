# @begin CS512_Phase_II @desc Display one or more greetings to the user.
# @in menu_csv @file file:menu.csv
# @out menu_cleaned @as menu_cleaned


    # @begin s1_openrefine_processing @desc OpenRefine Cleaning of physical_description
    # @in menu_csv @as menu_csv
    # @out menu_s1 @as menu_s1
    # @end s1_openrefine_processing

    # @begin s2_analyze_dq_issues @desc Analyze DQ Issues
    # @in menu_s1
    # @out dq_issues @as dq_issues
    # @end s2_analyze_dq_issues

    # @begin s3_process_physical_description_2 @desc Clean physical_descrption Phase 2
    # @in menu_s1
    # @in dq_issues
    # @out menu_s3_1 @as menu_s3_1
    # @end s3_process_physical_description_2

    # @begin s3_clean_location_data @desc Clean location_data
    # @in menu_s1
    # @in dq_issues
    # @out menu_s3_2 @as menu_s3_2
    # @end s3_clean_location_data

    # @begin s3_standardize_event @desc Standardize event Column
    # @in menu_s1
    # @in dq_issues
    # @out menu_s3_3 @as menu_s3_3
    # @end s3_standardize_event

    # @begin s3_remove_missing_values @desc Analyze DQ Issues
    # @in menu_s1
    # @in dq_issues
    # @out menu_s3_4 @as menu_s3_4
    # @end s3_remove_missing_values

    # @begin s3_merge @desc Merge Cleaning Tasks
    # @in menu_s3_1
    # @in menu_s3_2
    # @in menu_s3_3
    # @in menu_s3_4
    # @out menu_cleaned @as menu_cleaned @file file:menu_cleaned.csv
    # @end s3_merge

# @end CS512_Phase_II