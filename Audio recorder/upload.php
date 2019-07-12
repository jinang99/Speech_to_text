<?php

	$flag = 0;
	print_r($_FILES); //this will print out the received name, temp name, type, size, etc.
	$dirs =glob('C:/sphinx/final/wav/*', GLOB_ONLYDIR);  //Fetches the existing speaker directories
	foreach($dirs as $x)
	{

		$y = str_replace('C:/sphinx/final/wav/', '' , $x); 
		echo (explode("_", $y)[1] == $_POST['User']);
		//If user already exists, set flag
		if(explode("_", $y)[1] == $_POST['User'])
			{	$flag =1;
				echo "IN IF";
				$input = $_FILES['audio_data']['tmp_name'];
				$output = 'C:/sphinx/final/wav/'.$y.'/'.$_FILES['audio_data']['name'].uniqid().".wav"; //Saving the audio file
				echo "$output";
		//move the file from temp name to local folder using $output name
				move_uploaded_file($input, $output);

				$fp = fopen('C:/sphinx/final/'.$y.'.txt', 'a');
				fwrite($fp, $_FILES['audio_data']['name']."\n");
				fclose($fp);
				break;
			}
	}
	//If new user is found, make new directory
	if ($flag == 0){
			echo "IN ELSE";
			$dirs =glob('C:/sphinx/final/wav/*', GLOB_ONLYDIR);
			$dir = end($dirs);
			$dir = str_replace('C:/sphinx/final/wav/', '' , $dir);
			$dirarray = explode("_", $dir);
	
			$last_num = (int) $dirarray[0]; //Get the last prefixed number
			mkdir('C:/sphinx/final/wav/'.($last_num + 1)."_".$_POST['User']);
			$new = ($last_num + 1)."_".$_POST['User'];
			$input = $_FILES['audio_data']['tmp_name'];
			$output = 'C:/sphinx/final/wav/'.$new.'/'.$_FILES['audio_data']['name'].uniqid('',true).".wav"; //Saving the audio file
			echo "$output";
	//move the file from temp name to local folder using $output name
			move_uploaded_file($input, $output);

			$fp = fopen('C:/sphinx/final/'.$new.'.txt', 'a');
			fwrite($fp, $_FILES['audio_data']['name']."\n");
			fclose($fp);

	}

?>