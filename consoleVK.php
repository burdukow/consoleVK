#!/usr/bin/env php
<?php

$token = "c4b2c6adf669eae50bf6933c84ef29c5c73746963d833a6b3d02943e52f7f7de24090b4cc214380cd4bb0";

function send ($peer, $message, $token) {
	$params = array( 
 'message' => $message, 
 'peer_id' => $peer, 
 'random_id' => 0, 
 'v' => '5.120', 
 'access_token' => $token );
return file_get_contents('https://api.vk.com/method/messages.send?'.http_build_query($params));
}
function request($method, $params, $token) {
		$result = file_get_contents('https://api.vk.com/method/'.$method.'?'.http_build_query($params).'&access_token='.$token.'&v=5.120');
 
		return $result;
 	}

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
 
$what = readline(">>> \n");
if($what == 1) {
	$data = readline("Напишите команду: \n");
    $param = explode(" ", $data);
    echo "--- \n";
    
if($param[0] == "dialog") {
	if($param[1] == "-l") { 
	system('clear');
	while (true) {
		sleep(3); 
	$name = json_decode(request("users.get", ["user_ids" => $param[2]], $token));
	$first = $name->response[0]->first_name;
	$last = $name->response[0]->last_name;
	echo "\e[1m $first $last: \e[0m \n";
	$list = json_decode(request("messages.getHistory", ["user_id" => $param[2]], $token))->response->items;
	foreach($list as $messages) {
	$from .= "$messages->from_id: $messages->text \n";
	} 
	echo $from;
	$send = readline("Напишите сообщение... : \n");
	send($param[2], $send, $token);
	
	} 
	} 
	
if($param[1] == "-s") {
	echo send($param[2], $param[3], $token);
} 
} 

if ($param[0] == "friends") {
if ($param[1] == "-l") {
	$list = json_decode(request("friends.get", ["user_id" => $param[2], "order" => "name", "fields" => "city,domain"], $token))->response->items;
	foreach($list as $friends) {
$users .= "$friends->first_name $friends->last_name: $friends->id \n";
} 
echo $users;
}
}
}