#################################################### 1. SDL HEADER ################################################### 							
 							
scenario = "FingerMapping_SBS_T3_12.8mins_1A_TR4s"; 
#401 volumes                              																			
#default_formatted_text = true;							
							
default_background_color = 70,70,70;							
default_text_color = 0, 255, 255;							
default_font = "Tahoma";							
default_font_size = 35;	
default_volume = 1;

#scenario_type = fMRI_emulation; 	# either fMRI or fMRI_emulation, depending on whether the external device is present or not
scenario_type = fMRI; 
#scan_period = 1900; # off in fMRI mode
pulses_per_scan = 1;

pulse_code = 44;	

channels = 6;              # 1-8 channels (2 = stereo)
bits_per_sample = 16;		# the amount of data in each digital sound sample given in number of bits
sampling_rate = 48000;     # sample rate in Hertz			
		
							
################################################## 2. SDL Part ########################################							
							
begin;							

#######

## instructie EN
picture { text {caption = "
In a moment you will feel stimulations
on the fingertips of your left hand.
Please count the total number of interruptions
in the stimulations.

Please fixate the cross,
lie as still as possible. 

Keep your fingers in the same position,
touching the modules without pressure."
; }; x = 0; y = 0;							
} instructie_pic;	

## instructie NL
#picture { text {caption = "
#You"
#; font_size = 20;}; x = 0; y = 0;							
#} instructie_pic;	

## einde run EN
picture { text {caption = "This was the end of this scan."; }; x = 0; y = 0;							
} einde_pic;

## einde run NL
#picture { text {caption = "Dit was het einde van deze scan."; }; x = 0; y = 0;							
#} einde_pic;	

######	

## fixatie
picture { text{caption = "*"; font_size = 60; description = "Fix"; }; x = 0; y = 0;							
} fix_pic;	

## fixatie
picture { text{caption = "*"; font_size = 60; description = "Fix"; }; x = 0; y = 0;							
} default;	

#wavefile { filename = "25HzSine_6ch_15s_ch1.wav";}soundstim;
#wavefile { filename = "25HzSine_1ch_1s.wav";}soundstim;
#wavefile { filename = "25HzSine_1ch_2-9s.wav";}soundstim; #FOR TESTING
#wavefile { filename = "15_9_regularinterruptions.wav";}soundstim;
#wavefile { filename = "15_9_nointerruptions.wav";}soundstim;
#wavefile { filename = "15_9_unpredictable.wav";}soundstim;
#wavefile { filename = "15_2_unpredictable.wav";}soundstim;
#wavefile { filename = "30_5_unpredictable.wav";}soundstim;
#wavefile { filename = "3p9s_0Int.wav";}soundstim;

	#sound { wavefile soundstim; speakers = 1; description = "module1"; default_code = "module1"; }module1_audio;#d1 speaker 3
	#sound { wavefile soundstim; speakers = 2; description = "module2"; default_code = "module2"; }module2_audio;#d2 speaker 6
	#sound { wavefile soundstim; speakers = 5; description = "module3"; default_code = "module3"; }module3_audio;#d3 speaker 5
	#sound { wavefile soundstim; speakers = 6; description = "module4"; default_code = "module6"; }module4_audio;#d4 speaker 2
	#sound { wavefile soundstim; speakers = 3; description = "module5"; default_code = "module5"; }module5_audio;#d5 speaker 1
	#sound { wavefile soundstim; speakers = 4; description = "module6"; default_code = "module4"; }module6_audio;#

array {

	sound { wavefile {filename = "3p9s_0Int.wav";}; speakers = 3; description = "D1_0Int"; default_code = "D1_0Int"; }D1_0Int_audio; 
	sound { wavefile {filename = "3p9s_1IntA.wav";}; speakers = 3; description = "D1_1Int"; default_code = "D1_1Int"; }D1_1IntA_audio;
	sound { wavefile {filename = "3p9s_1IntB.wav";}; speakers = 3; description = "D1_1Int"; default_code = "D1_1Int"; }D1_1IntB_audio;
	sound { wavefile {filename = "3p9s_1IntC.wav";}; speakers = 3; description = "D1_1Int"; default_code = "D1_1Int"; }D1_1IntC_audio;
	sound { wavefile {filename = "3p9s_1IntD.wav";}; speakers = 3; description = "D1_1Int"; default_code = "D1_1Int"; }D1_1IntD_audio;
	sound { wavefile {filename = "3p9s_2IntA.wav";}; speakers = 3; description = "D1_2Int"; default_code = "D1_2Int"; }D1_2IntA_audio;
	sound { wavefile {filename = "3p9s_2IntB.wav";}; speakers = 3; description = "D1_2Int"; default_code = "D1_2Int"; }D1_2IntB_audio;
	sound { wavefile {filename = "3p9s_2IntC.wav";}; speakers = 3; description = "D1_2Int"; default_code = "D1_2Int"; }D1_2IntC_audio;
	sound { wavefile {filename = "3p9s_3Int.wav";}; speakers = 3; description = "D1_3Int"; default_code = "D1_3Int"; }D1_3Int_audio;
}sounds_D1;

array {

	sound { wavefile {filename = "3p9s_0Int.wav";}; speakers = 6; description = "D2_0Int"; default_code = "D2_0Int"; };
	sound { wavefile {filename = "3p9s_1IntA.wav";}; speakers = 6; description = "D2_1Int"; default_code = "D2_1Int"; };
	sound { wavefile {filename = "3p9s_1IntB.wav";}; speakers = 6; description = "D2_1Int"; default_code = "D2_1Int"; };
	sound { wavefile {filename = "3p9s_1IntC.wav";}; speakers = 6; description = "D2_1Int"; default_code = "D2_1Int"; };
	sound { wavefile {filename = "3p9s_1IntD.wav";}; speakers = 6; description = "D2_1Int"; default_code = "D2_1Int"; };
	sound { wavefile {filename = "3p9s_2IntA.wav";}; speakers = 6; description = "D2_2Int"; default_code = "D2_2Int"; };
	sound { wavefile {filename = "3p9s_2IntB.wav";}; speakers = 6; description = "D2_2Int"; default_code = "D2_2Int"; };
	sound { wavefile {filename = "3p9s_2IntC.wav";}; speakers = 6; description = "D2_2Int"; default_code = "D2_2Int"; };
	sound { wavefile {filename = "3p9s_3Int.wav";}; speakers = 6; description = "D2_3Int"; default_code = "D2_3Int"; };
}sounds_D2;

array {

	sound { wavefile {filename = "3p9s_0Int.wav";}; speakers = 5; description = "D3_0Int"; default_code = "D3_0Int"; };
	sound { wavefile {filename = "3p9s_1IntA.wav";}; speakers = 5; description = "D3_1Int"; default_code = "D3_1Int"; };
	sound { wavefile {filename = "3p9s_1IntB.wav";}; speakers = 5; description = "D3_1Int"; default_code = "D3_1Int"; };
	sound { wavefile {filename = "3p9s_1IntC.wav";}; speakers = 5; description = "D3_1Int"; default_code = "D3_1Int"; };
	sound { wavefile {filename = "3p9s_1IntD.wav";}; speakers = 5; description = "D3_1Int"; default_code = "D3_1Int"; };
	sound { wavefile {filename = "3p9s_2IntA.wav";}; speakers = 5; description = "D3_2Int"; default_code = "D3_2Int"; };
	sound { wavefile {filename = "3p9s_2IntB.wav";}; speakers = 5; description = "D3_2Int"; default_code = "D3_2Int"; };
	sound { wavefile {filename = "3p9s_2IntC.wav";}; speakers = 5; description = "D3_2Int"; default_code = "D3_2Int"; };
	sound { wavefile {filename = "3p9s_3Int.wav";}; speakers = 5; description = "D3_3Int"; default_code = "D3_3Int"; };
}sounds_D3;

array {

	sound { wavefile {filename = "3p9s_0Int.wav";}; speakers = 2; description = "D4_0Int"; default_code = "D4_0Int"; };
	sound { wavefile {filename = "3p9s_1IntA.wav";}; speakers = 2; description = "D4_1Int"; default_code = "D4_1Int"; };
	sound { wavefile {filename = "3p9s_1IntB.wav";}; speakers = 2; description = "D4_1Int"; default_code = "D4_1Int"; };
	sound { wavefile {filename = "3p9s_1IntC.wav";}; speakers = 2; description = "D4_1Int"; default_code = "D4_1Int"; };
	sound { wavefile {filename = "3p9s_1IntD.wav";}; speakers = 2; description = "D4_1Int"; default_code = "D4_1Int"; };
	sound { wavefile {filename = "3p9s_2IntA.wav";}; speakers = 2; description = "D4_2Int"; default_code = "D4_2Int"; };
	sound { wavefile {filename = "3p9s_2IntB.wav";}; speakers = 2; description = "D4_2Int"; default_code = "D4_2Int"; };
	sound { wavefile {filename = "3p9s_2IntC.wav";}; speakers = 2; description = "D4_2Int"; default_code = "D4_2Int"; };
	sound { wavefile {filename = "3p9s_3Int.wav";}; speakers = 2; description = "D4_3Int"; default_code = "D4_3Int"; };
}sounds_D4;

array {

	sound { wavefile {filename = "3p9s_0Int.wav";}; speakers = 1; description = "D5_0Int"; default_code = "D5_0Int"; };
	sound { wavefile {filename = "3p9s_1IntA.wav";}; speakers = 1; description = "D5_1Int"; default_code = "D5_1Int"; };
	sound { wavefile {filename = "3p9s_1IntB.wav";}; speakers = 1; description = "D5_1Int"; default_code = "D5_1Int"; };
	sound { wavefile {filename = "3p9s_1IntC.wav";}; speakers = 1; description = "D5_1Int"; default_code = "D5_1Int"; };
	sound { wavefile {filename = "3p9s_1IntD.wav";}; speakers = 1; description = "D5_1Int"; default_code = "D5_1Int"; };
	sound { wavefile {filename = "3p9s_2IntA.wav";}; speakers = 1; description = "D5_2Int"; default_code = "D5_2Int"; };
	sound { wavefile {filename = "3p9s_2IntB.wav";}; speakers = 1; description = "D5_2Int"; default_code = "D5_2Int"; };
	sound { wavefile {filename = "3p9s_2IntC.wav";}; speakers = 1; description = "D5_2Int"; default_code = "D5_2Int"; };
	sound { wavefile {filename = "3p9s_3Int.wav";}; speakers = 1; description = "D5_3Int"; default_code = "D5_3Int"; };
}sounds_D5;

### trials	###

## instructie begin
trial {						
       trial_duration = stimuli_length;
		 picture instructie_pic;							
       code = "Instructie";							
} instructie_trial;

## einde
trial {											
		 stimulus_event{						
       picture einde_pic;
       duration=4000;             
         } einde_stim;
       } einde_trial; 

trial { 
	trial_mri_pulse = 1;
	trial_duration = stimuli_length; 							
	stimulus_event { picture fix_pic; code = "Rest"; } fix_stimulus;      # forever; rest wordt er overheen geprojecteerd						
} fix_trial;

## grijze rechthoek, eerste baseline
trial { 							
	trial_mri_pulse = 1;
	trial_duration = 8000;
	stimulus_event { picture fix_pic; code = "Baseline"; } stim_fix_stimulus;      # forever; rest wordt er overheen geprojecteerd						
} stim_fix_trial;

## stimulation trial; wordt aangepast op basis van randomisatie
trial {
	trial_mri_pulse = 1;
	stimulus_event {
		sound D1_0Int_audio;
		deltat = 0;
		#duration = 4000;
	}stim_snd;
}stimulation_trial;

						
############################################################# 3. PCL ###################################################							
							
begin_pcl;	
##CHANGE BEFORE SCANNING

array <int> rest_duration[4]={2, 2, 2, 2};

int pulse_update = 0;

int TR=	2000	;													
int stim_duration = 		2	;#*TR;												
int total_nr_trials =		150	;												
#int total_nr_trials = 5;
													
array <int> finger [total_nr_trials] = 	{	2,4,5,4,5,4,3,8,2,8,5,4,3,8,5,8,4,5,2,8,3,1,5,8,3,1,8,3,8,1,2,5,1,8,5,1,2,4,8,1,3,5,3,4,2,1,3,5,8,3,4,2,4,2,5,1,3,2,1,2,4,8,3,8,2,3,5,1,8,4,3,5,1,8,4,8,3,5,1,2,1,2,1,4,8,5,8,1,5,8,2,8,1,3,2,3,2,3,1,3,2,8,4,1,5,3,5,4,1,3,2,3,8,4,3,8,4,1,4,1,8,5,4,8,2,5,8,2,4,5,4,3,5,2,8,1,8,2,3,5,4,8,1,2,8,5,1,4,2,4};
#array <int> finger [total_nr_trials] = { 1, 2, 3, 4, 5}; 

		
array <string> modules[4][5] = { {"D1_0Int", "D2_0Int", "D3_0Int", "D4_0Int", "D5_0Int"},
											{"D1_1Int", "D2_1Int", "D3_1Int", "D4_1Int", "D5_1Int"},
											{"D1_2Int", "D2_2Int", "D3_2Int", "D4_2Int", "D5_2Int"},
											{"D1_3Int", "D2_3Int", "D3_3Int", "D4_3Int", "D5_3Int"}};


		
## start of actual trials							
			
instructie_trial.present();							
#stim_fix_trial.set_duration(9500); #should be 9500
stim_fix_trial.present();	
pulse_update = pulse_manager.main_pulse_count()+ 2;
stimulation_trial.set_mri_pulse(pulse_update);				

	int i = 1;		
	int intercount = 0;				
	loop 	
	until i > total_nr_trials						
							
	begin						
		
			if finger[i] < 7 then
				
				int randnr = random(1,9);
				
				
				if randnr > 1 && randnr < 6 then 
					stim_snd.set_event_code(modules[2][finger[i]]);
				elseif randnr > 5 && randnr < 9 then 
					stim_snd.set_event_code(modules[3][finger[i]]);
				elseif randnr == 9 then 
					stim_snd.set_event_code(modules[4][finger[i]]);
				else
					stim_snd.set_event_code(modules[1][finger[i]]);
				end;
				
				if finger[i] == 1 then
					stim_snd.set_stimulus(sounds_D1[randnr]);
				elseif finger[i] == 2 then 
					stim_snd.set_stimulus(sounds_D2[randnr]);
				elseif finger[i] == 3 then 
					stim_snd.set_stimulus(sounds_D3[randnr]);
				elseif finger[i] == 4 then 
					stim_snd.set_stimulus(sounds_D4[randnr]);
				elseif finger[i] == 5 then 
					stim_snd.set_stimulus(sounds_D5[randnr]);
				end;
				
				stimulation_trial.present(); 
				pulse_update = pulse_update + stim_duration;
				fix_trial.set_mri_pulse(pulse_update);
				stimulation_trial.set_mri_pulse(pulse_update);
			
		elseif finger[i] >6  then
				fix_trial.present();
				pulse_update = pulse_update + 2;
				stimulation_trial.set_mri_pulse(pulse_update);
												
			end;
														
		i = i + 1;					
 							
	end;
	fix_trial.set_duration(rest_duration[1]*TR*5); #to get 10 volumes of rest at the end
	fix_trial.present();



			