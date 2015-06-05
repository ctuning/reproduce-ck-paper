call ck cp experiment:demo-autotune-compiler-flags-susan-android-i100 experiment:demo-autotune-flags-susan-android-pareto
call ck autotune pipeline:program pipeline_from_file=_setup_program_pipeline_tmp.json @autotune_program_pipeline_i100_apply_pareto.json
