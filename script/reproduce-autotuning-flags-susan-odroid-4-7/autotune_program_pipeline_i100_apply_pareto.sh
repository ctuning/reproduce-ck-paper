ck cp experiment:demo-autotune-compiler-flags-susan-odroid-0-3-i100 :demo-autotune-flags-susan-odroid-0-3-pareto
ck autotune pipeline:program pipeline_from_file=_setup_program_pipeline_tmp.json @autotune_program_pipeline_i100_apply_pareto.json
