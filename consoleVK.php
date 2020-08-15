#!/usr/bin/env php
<?php

require_once "functions.php";

system('figlet consoleVK');

 echo "\e[1m consoleVK \e[0m \n";
 echo "\e[1m version: 1.0 \e[0m \n";
 echo "\e[1m author's: Lthgt, brdkv \e[0m \n";
 echo "  ";
 echo "
 1) console
 2) help
 3) exit
";

$token = json_decode(file_get_contents("config.json"))->token;
echo "TOKEN: ". $token;

$api = new \api\functions($token, 5.122);
$what = readline(">>> \n");

echo "--- \n";

if ($what == 1) 
{
	$data   = readline("Напишите команду: \n");
    $param  = explode(" ", $data);
    $comand = $param[0];
    $flag   = $param[1];
	
		if($comand == "dialog")
		{
			/* if($flag == "-l")
			{ 
				system('clear');
					while (true)
					{
						sleep(3); 
						$name = json_decode($api->request("users.get", ["user_ids" => $param[2]], $token));

						$first = $name->response[0]->first_name;
						$last  = $name->response[0]->last_name;

						echo "\e[1m $first $last: \e[0m \n";

						$list = json_decode(request("messages.getHistory", ["user_id" => $param[2]], $token))->response->items;
							foreach($list as $messages)
							{

							$from .= "$messages->from_id: $messages->text \n";
						} 
						echo $from;
						$send = readline("Напишите сообщение... : \n");
						send($param[2], $send, $token);
	
			} 
		} */
	
		if($flag == "-s")
		{
		echo $param[2];
		echo $param[3];
		echo $api->sendMessage($param[2], $param[3]);
			} 
		}
	
		if ($comand == "friends")
		{
			if ($flag == "-l")
			{
				echo $api->friendsList($param[2]);
				}
			}
		}
	
    
