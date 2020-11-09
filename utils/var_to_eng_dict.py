

var_to_eng = {
	'batch' : 'Batch_ExtractionID',
	'bloom' : 'Bloom',
	'viscosidad' : 'Viscosity',
	'claridad' : 'Clarity',
	'averageproduction' : 'Average_Production',
	'yield' : 'Yield',
	'd03_amn_carnaza' : 'RawMaterial_Carnaza',
	'd03_vap_press' : 'RawMaterial_Press',
	'd03_carnaza' : 'put_english_name ',
	'd03_cuero' : 'put_english_name ',
	'd03_orillo' : 'put_english_name ',
	'd03_patica' : 'put_english_name ',
	'd03_vaqueta' : 'put_english_name ',
	'd04_ph_initial_liq' : 'ph_Light_Liquor',
	'd04_clarity_initial_liq' : 'Clarity_Light_Liquor',
	'd04_total_residue' : 'Total_Residue_All_Reactors_in',
	'd04_extract_duration' : 'Extraction_Duration_h',
	'd05_peroxido_hid' : 'Hydrogen_Peroxide_ppm',
	'd05_dioxido_azufre' : 'Sulfur_Dioxide_ppm',
	'd05_ntu_l1' : 'Clarity_Light_Liquor_Tank1_NTU',
	'd05_ntu_l3' : 'Clarity_Light_Liquor_Tank3_NTU',
	'd05_ntu_fp1' : 'Clarity_Liquor_Press_Filter1',
	'd05_ntu_fp2' : 'Clarity_Liquor_Press_Filter2',
	'd05_ntu_fp4' : 'Clarity_Liquor_Press_Filter4',
	'd06_pht' : 'put_english_name ',
	'd06_phuf2' : 'put_english_name ',
	'd09_t_condensing' : 'Condensing_Temperature',
	'd09_t_leg' : 'Liquor_Temp_Separator_Leg',
	'd09_t_liquor' : 'Heavy_Liquor_Temp',
	'd09_conc_liquor' : 'Heavy_Liquor_Concentration',
	'd09_tri_freca' : 'Triplex_A_Frequency',
	'd09_tri_frecb' : 'Triplex_B_Frequency',
	'd09_tri_frecd' : 'Triplex_D_Frequency',
	'd10_t_esteril' : 'put_english_name ',
	'd10_t_out_gelatin' : 'put_english_name ',
	'd10_t_out_water' : 'put_english_name ',
	'd10_p_vaccum' : 'put_english_name ',
	'd11_ts_ref' : 'put_english_name ',
	'd11_td_ref' : 'put_english_name ',
	'd12_p_exch_water' : 'put_english_name ',
	'd12_kath_lvl' : 'put_english_name ',
	'd12_p_atom_cond' : 'put_english_name ',
	'd12_p_atom_regn' : 'put_english_name ',
	'd12_p_filt' : 'put_english_name ',
	'd12_p_cond' : 'put_english_name ',
	'd12_p_regen' : 'put_english_name ',
	'd12_ta' : 'put_english_name ',
	'd12_tb' : 'put_english_name ',
	'd12_td' : 'put_english_name ',
	'd14_vpa' : 'put_english_name ',
	'd14_vpb' : 'put_english_name ',
	'd14_vpd' : 'put_english_name ',
	'd14_t2a' : 'put_english_name ',
	'd14_t2b' : 'put_english_name ',
	'd14_t2d' : 'put_english_name ',
	'd14_t3a' : 'put_english_name ',
	'd14_t3b' : 'put_english_name ',
	'd14_3d' : 'put_english_name ',
	'd14_t4a' : 'put_english_name ',
	'd14_t4b' : 'put_english_name ',
	'd14_t4d' : 'put_english_name ',
	'd14_t5a' : 'put_english_name ',
	'd14_t5b' : 'put_english_name ',
	'd14_t5d' : 'put_english_name ',
	'd14_t6a' : 'put_english_name ',
	'd14_t6b' : 'put_english_name ',
	'd14_t6d' : 'put_english_name ',
	'd14_t7a' : 'put_english_name ',
	'd14_t7b' : 'put_english_name ',
	'd14_t7d' : 'put_english_name '
}

var_to_process_dict = {
	'batch' : 'ExtractionID',
	'bloom' : 'Result_Variable',
	'viscosidad' : 'Result_Variable',
	'claridad' : 'Result_Variable',
	'averageproduction' : 'Result_Variable',
	'yield' : 'Result_Variable',
	'd03_amn_carnaza' : 'put_process_name ',
	'd03_vap_press' : 'put_process_name ',
	'd03_carnaza' : 'put_process_name ',
	'd03_cuero' : 'put_process_name ',
	'd03_orillo' : 'put_process_name ',
	'd03_patica' : 'put_process_name ',
	'd03_vaqueta' : 'put_process_name ',
	'd04_ph_initial_liq' : 'Extraction_Control',
	'd04_clarity_initial_liq' : 'Extraction_Control',
	'd04_total_residue' : 'Extraction_Control',
	'd04_extract_duration' : 'Extraction_Control',
	'd05_peroxido_hid' : 'Physicochemical Control',
	'd05_dioxido_azufre' : 'Physicochemical Control',
	'd05_ntu_l1' : 'Physicochemical Control',
	'd05_ntu_l3' : 'Physicochemical Control',
	'd05_ntu_fp1' : 'Physicochemical Control',
	'd05_ntu_fp2' : 'Physicochemical Control',
	'd05_ntu_fp4' : 'Physicochemical Control',
	'd06_pht' : 'put_process_name ',
	'd06_phuf2' : 'put_process_name ',
	'd09_t_condensing' : 'Paraflash_Control',
	'd09_t_leg' : 'Paraflash_Control',
	'd09_t_liquor' : 'Paraflash_Control',
	'd09_conc_liquor' : 'Paraflash_Control',
	'd09_tri_freca' : 'Paraflash_Control',
	'd09_tri_frecb' : 'Paraflash_Control',
	'd09_tri_frecd' : 'Paraflash_Control',
	'd10_t_esteril' : 'put_process_name ',
	'd10_t_out_gelatin' : 'put_process_name ',
	'd10_t_out_water' : 'put_process_name ',
	'd10_p_vaccum' : 'put_process_name ',
	'd11_ts_ref' : 'put_process_name ',
	'd11_td_ref' : 'put_process_name ',
	'd12_p_exch_water' : 'put_process_name ',
	'd12_kath_lvl' : 'put_process_name ',
	'd12_p_atom_cond' : 'put_process_name ',
	'd12_p_atom_regn' : 'put_process_name ',
	'd12_p_filt' : 'put_process_name ',
	'd12_p_cond' : 'put_process_name ',
	'd12_p_regen' : 'put_process_name ',
	'd12_ta' : 'put_process_name ',
	'd12_tb' : 'put_process_name ',
	'd12_td' : 'put_process_name ',
	'd14_vpa' : 'put_process_name ',
	'd14_vpb' : 'put_process_name ',
	'd14_vpd' : 'put_process_name ',
	'd14_t2a' : 'put_process_name ',
	'd14_t2b' : 'put_process_name ',
	'd14_t2d' : 'put_process_name ',
	'd14_t3a' : 'put_process_name ',
	'd14_t3b' : 'put_process_name ',
	'd14_3d' : 'put_process_name ',
	'd14_t4a' : 'put_process_name ',
	'd14_t4b' : 'put_process_name ',
	'd14_t4d' : 'put_process_name ',
	'd14_t5a' : 'put_process_name ',
	'd14_t5b' : 'put_process_name ',
	'd14_t5d' : 'put_process_name ',
	'd14_t6a' : 'put_process_name ',
	'd14_t6b' : 'put_process_name ',
	'd14_t6d' : 'put_process_name ',
	'd14_t7a' : 'put_process_name ',
	'd14_t7b' : 'put_process_name ',
	'd14_t7d' : 'put_process_name '
}