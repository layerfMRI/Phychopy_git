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
#scan_period =2000; # comment out in fMRI mode
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
on your index, middle and ring finger
of the right hand.

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

wavefile { filename = "30_5_unpredictable.wav";}soundstim;
#wavefile { filename = "chirp_32-1Hz.wav";}soundstim;
#wavefile { filename = "audio5CH.wav";}soundstim;

array {

	sound { wavefile soundstim;  speakers = 6; description = "module1"; default_code = "module1"; }module1_audio;#
	sound { wavefile soundstim;  speakers = 6; description = "module2"; default_code = "module2"; }module2_audio;#d3
	sound { wavefile soundstim;  speakers = 6; description = "module3"; default_code = "module3"; }module3_audio;#d4
	sound { wavefile soundstim;  speakers = 6; description = "module4"; default_code = "module6"; }module4_audio;
	sound { wavefile soundstim;  speakers = 6; description = "module5"; default_code = "module5"; }module5_audio;
	sound { wavefile soundstim;  speakers = 6; description = "module6"; default_code = "module4"; }module6_audio;

	#sound { wavefile { filename = "module1_3p8s.wav"; }; description = "module1"; default_code = "module1"; }module1_audio;
	#sound { wavefile { filename = "module2_3p8s.wav"; }; description = "module2"; default_code = "module2"; }module2_audio;
	#sound { wavefile { filename = "module3_3p8s.wav"; }; description = "module3"; default_code = "module3"; }module3_audio;
	#sound { wavefile { filename = "module4_3p8s.wav"; }; description = "module4"; default_code = "module4"; }module4_audio;
	#sound { wavefile { filename = "module5_3p8s.wav"; }; description = "module5"; default_code = "module5"; }module5_audio;
	#sound { wavefile { filename = "module6_3p8s.wav"; }; description = "module6"; default_code = "module6"; }module6_audio;
}sounds;

#sound { wavefile { filename = "silence_2sec_6ch_48k.wav"; }; description = "silence"; default_code = "silence"; }silence;


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
	stimulus_event { 
		picture fix_pic; 
		code = "Baseline"; 
		duration = 31582;
	} fix_stimulus;      # forever; rest wordt er overheen geprojecteerd						
} fix_trial;

## grijze rechthoek, eerste baseline
trial { 							
	trial_mri_pulse = 1;
	trial_duration = stimuli_length;
	stimulus_event { 
		picture fix_pic; 
		code = "Baseline"; 
		duration = 31582;
	} first_fix_stimulus;      # forever; rest wordt er overheen geprojecteerd								
} stim_fix_trial; #this is the first baseline!!! check desired duration

## stimulation trial; wordt aangepast op basis van randomisatie
trial {
	trial_mri_pulse = 1;
	stimulus_event {
		sound module1_audio;
		deltat = 0;
		duration = 30000;
	}stim_snd;
}stimulation_trial;

						
############################################################# 3. PCL ###################################################							
							
begin_pcl;	
##CHANGE BEFORE SCANNING

array <int> rest_duration[4]={8, 8, 8, 8};
#array <int> rest_duration[4]={1, 1, 1,1};
 
int pulse_update = 0;

int TR=	3888	;													
int stim_duration = 		8;	#*TR;												
int total_nr_trials =		50	;												
#run1A															
array <int> finger [total_nr_trials] = 	{	3, 8,	2, 8,	4, 8,	3, 8,	2, 8,	4, 8,	3, 8,	2, 8,	4, 8,	2, 8,	4, 8,	3, 8,	3, 8,	2, 8,	4, 8,	3, 8,	2, 8,	4, 8,	3, 8,	2, 8,	4, 8,	2, 8,	4, 8,	3, 8,	7, 7	};
#run1B															
#array <int> finger [total_nr_trials] = 	{	3, 8,	1, 8,	2, 8,	1, 8,	2, 8,	3, 8,	1, 8,	2, 8,	3, 8,	1, 8,	2, 8,	3, 8,	7	};
#run2A															
#array <int> finger [total_nr_trials] = 	{	1, 8,	2, 8,	1, 8,	2, 8,	3, 8,	1, 8,	3, 8,	2, 8,	1, 8,	3, 8,	3, 8,	2, 8,	7	};
#run2B															
#array <int> finger [total_nr_trials] = 	{	2, 8,	3, 8,	3, 8,	1, 8,	2, 8,	3, 8,	1, 8,	3, 8,	2, 8,	1, 8,	2, 8,	1, 8,	7	};

		
#array <string> modules[6]={"R D2 tip", "R D3 tip", "R D4 tip", "R D2 base", "R D3 base", "R D4 base"	};#{"module1", "module2", "module3", "module4", "module5", "module6"	};
array <string> modules[6]={"R D1 tip", "R D2 tip", "R D3 tip", "R D4 tip", "R D5 tip", "nothing"	};

		
## start of actual trials							
			
instructie_trial.present();							
#stim_fix_trial.set_duration(9500); #should be 9500
stim_fix_trial.present();	#FIRST BASELINE check which length is desired for the first fixation, currently 30 s
#pulse_update = pulse_manager.main_pulse_count()+ 2;

#fix_trial.set_mri_pulse(pulse_update);	
#fix_trial.set_duration(rest_duration[1]*TR);
#fix_trial.present();	
		
#stimulation_trial.set_mri_pulse(pulse_update);	

	int i = 1;						
	loop 	
	until i > total_nr_trials						
							
	begin						
		
			if finger[i] < 7 then
				stim_snd.set_event_code(modules[finger[i] ]);#for the logfile
				stim_snd.set_stimulus(sounds[finger[i]]); #set the sound (i.e. finger)
				#stim_fix_trial.set_mri_pulse(pulse_manager.main_pulse_count() + 1);
				#stim_fix_trial.set_duration(20);
				#stim_fix_trial.present();		
				stimulation_trial.present(); 
				#pulse_update = pulse_update + 2*stim_duration;
				#fix_trial.set_mri_pulse(pulse_update);
	
			
		elseif finger[i] > 6  then
				fix_trial.present();
				#pulse_update = pulse_update + 2*rest_duration[finger[i] -6];
				#stimulation_trial.set_mri_pulse(pulse_update);
				#fix_trial.set_duration(rest_duration[finger[i] -6]);
				#fix_trial.present();
												
			end;
														
		i = i + 1;					
 							
	end;
	#fix_trial.set_duration(rest_duration[1]*TR);
	fix_trial.present();
	fix_trial.present();


#einde_trial.present();
			