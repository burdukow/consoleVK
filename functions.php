<?php
/**
 * project: ConsoleVK
 * author: Lthgt <mail@masterovv.ru>
 */

namespace api;

class functions
{
	var $token;
	var $version;
	
	function __construct($token, $version)
	{
		$this->token = $token;
		$this->version = $version;
	}

	function vk_api($method, $params)
	{
		$result = file_get_contents('https://api.vk.com/method/'.$method.'?'.http_build_query($params).'&access_token='.$this->token.'&v='.$this->version);
 
		return $result;
 	}

 	function sendMessage($peer_id, $message)
 	{

 		$result = $this->vk_api("messages.send", ['message'=>$message,'peer_id'=>$peer_id,'random_id'=>0,'v'=>$this->version,'access_token'=>$this->token]);

		return $result;
	}

	function friendsList($user_id)
	{
		$data = json_decode($this->request("friends.get",["user_id"=>$user_id,"order"=>"name","fields"=>"city,domain"]))->response->items;
		foreach($data as $friends)
		{
			$result .= "$friends->first_name $friends->last_name: $friends->id \n";

			return $result;
		}
	} 
}