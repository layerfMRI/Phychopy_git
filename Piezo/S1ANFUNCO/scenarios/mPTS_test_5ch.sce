#################################################### 1. SDL HEADER ################################################### 							
 							
scenario = "BrainEXPain_sound";                               							
active_buttons = 1;							
button_codes = 1;  							
response_matching = simple_matching;													
#default_formatted_text = true;							
							
default_background_color = 70,70,70;							
default_text_color = 0, 255, 255;							
default_font = "Tahoma";							
default_font_size = 30;	

channels = 6;              # 1-8 channels (2 = stereo)
bits_per_sample = 16;		# the amount of data in each digital sound sample given in number of bits
sampling_rate = 48000;     # sample rate in Hertz							
							
################################################## 2. SDL Part ########################################							
							
begin;							


## instructie begin
picture { text {caption = "TEST - press space"; font_size = 30;}; x = 0; y = 0;							
} instructie_pic;	

## fixatie
picture { text{caption = "*"; font_size = 60; description = "Fix"; }; x = 0; y = 0;							
} fix_pic;	

picture { text{caption = "*"; font_size = 60; font_color = 255, 0, 0; description = "Fix"; }; x = 0; y = 0;							
} stim;	
picture { text{caption = "thumb tip"; font_size = 60; font_color = 255, 0, 0; description = "Fix"; }; x = 0; y = 0;							
} stim1;	
picture { text{caption = "index tip"; font_size = 60; font_color = 255, 0, 0; description = "Fix"; }; x = 0; y = 0;							
} stim2;	
picture { text{caption = "middle tip"; font_size = 60; font_color = 255, 0, 0; description = "Fix"; }; x = 0; y = 0;							
} stim3;	
picture { text{caption = "ring tip"; font_size = 60; font_color = 255, 0, 0; description = "Fix"; }; x = 0; y = 0;							
} stim4;	
picture { text{caption = "pinky tip"; font_size = 60; font_color = 255, 0, 0; description = "Fix"; }; x = 0; y = 0;							
} stim5;	
picture { text{caption = "ring base"; font_size = 60; font_color = 255, 0, 0; description = "Fix"; }; x = 0; y = 0;							
} stim6;	

#picture { text{caption = "index base"; font_size = 60; font_color = 255, 0, 0; description = "Fix"; }; x = 0; y = 0;							
#} stim4;	
#picture { text{caption = "middle base"; font_size = 60; font_color = 255, 0, 0; description = "Fix"; }; x = 0; y = 0;							
#} stim5;	


#wavefile { filename = "25HzSine_6ch_15s_ch1.wav";}soundstim;
#wavefile { filename = "audio5CH.wav";}soundstim;
#wavefile { filename = "25HzSine_1ch_1s.wav";}soundstim;
#wavefile { filename = "30_5_unpredictable.wav";}soundstim; #FOR TESTING
#wavefile { filename = "25HzSine_1ch_2-9s.wav";}soundstim; #FOR TESTING
#wavefile { filename = "5_8_regularinterruptions.wav";}soundstim; #FOR TESTING
#wavefile { filename = "5_8_nointerruptions.wav";}soundstim; #FOR TESTING
#wavefile { filename = "14_8_regularinterruptions.wav";}soundstim; #FOR TESTING
#wavefile { filename = "14_8_nointerruptions.wav";}soundstim; #FOR TESTING
#wavefile { filename = "predictable.wav";}soundstim; #FOR TESTING
#wavefile { filename = "unpredictable.wav";}soundstim; #FOR TESTING
#wavefile { filename = "7_9_unpredictable.wav";}soundstim; #FOR TESTING
#wavefile { filename = "15_9_unpredictable.wav";}soundstim; #FOR TESTING
#wavefile { filename = "chirp_32-1Hz.wav";}soundstim;
wavefile { filename = "30_5_unpredictable.wav";}soundstim;

array {

	sound { wavefile soundstim; description = "module1"; default_code = "module1"; }module1_audio;#d1 speaker 3
	sound { wavefile soundstim;  description = "module2"; default_code = "module2"; }module2_audio;#d2 speaker 6
	sound { wavefile soundstim;  description = "module3"; default_code = "module3"; }module3_audio;#d3 speaker 5
	sound { wavefile soundstim; description = "module4"; default_code = "module6"; }module4_audio;#d4 speaker 2
	sound { wavefile soundstim;  description = "module5"; default_code = "module5"; }module5_audio;#d5 speaker 1
	sound { wavefile soundstim;  description = "module6"; default_code = "module4"; }module6_audio;#
}sounds;

### trials	###

## instructie begin
trial {trial_duration = forever;             				
       trial_type = specific_response;					
       terminator_button = 1;							
       picture instructie_pic;							
       code = "Instructie_hand";						
} instructie1_trial;

## grijze rechthoek, eerste baseline
trial { 							
	trial_duration = stimuli_length;
	stimulus_event { picture fix_pic; code = "First_fix"; } first_fix_stimulus;      		
} fix_trial;

## stimulation trial; wordt aangepast op basis van randomisatie
trial {
	stimulus_event {
		sound module1_audio;
		code = "sound";
		deltat = 0;
	}stim_snd;
	stimulus_event {
		picture stim;
		code = "stim";
	}stim_pic;
}stimulation_trial;

							
############################################################# 3. PCL ###################################################							
							
begin_pcl;							
							
int total_nr_trials = 5;


## veranderen op basis van randomisatie!!
array <int> finger [total_nr_trials] = { 1, 2, 3, 4, 5}; 
					
## start of actual trials							
						
instructie1_trial.present();
fix_trial.set_duration(3000);
fix_trial.present();					

	int i = 1;						
	loop 	
	until i > total_nr_trials
							
	begin						
			if finger[i] == 1 then
				stim_snd.set_stimulus(module1_audio);
				stim_snd.set_event_code("thumb tip");
				stim_pic.set_stimulus(stim1);
				stim_pic.set_event_code("thumb tip");			

			elseif finger[i] == 2 then
				stim_snd.set_stimulus(module2_audio);
				stim_snd.set_event_code("index tip");
				stim_pic.set_stimulus(stim2);
				stim_pic.set_event_code("index tip");
				
	
			elseif finger[i] == 3 then
				stim_snd.set_stimulus(module3_audio);
				stim_snd.set_event_code("middle tip");
				stim_pic.set_stimulus(stim3);
				stim_pic.set_event_code("middle tip");
			
			elseif finger[i] == 4 then
				stim_snd.set_stimulus(module4_audio);
				stim_snd.set_event_code("ring tip");
				stim_pic.set_stimulus(stim4);
				stim_pic.set_event_code("ring tip");
				
			elseif finger[i] == 5 then
				stim_snd.set_stimulus(module5_audio);
				stim_snd.set_event_code("pinky base");
				stim_pic.set_stimulus(stim5);
				stim_pic.set_event_code("pinky base");
				
			elseif finger[i] == 6 then
				stim_snd.set_stimulus(module6_audio);
				stim_snd.set_event_code("ring base");
				stim_pic.set_stimulus(stim6);
				stim_pic.set_event_code("ring base");
				
			end; 

		stimulation_trial.present(); 
		
		fix_trial.set_duration(3000);
		fix_trial.present();					
			
		i = i + 1;					
							
	end;
	