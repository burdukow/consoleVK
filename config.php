<?php
require_once "functions.php";

echo "Enter the VK authorization token \n";
echo "you can get it by following the link:";
echo "https://oauth.vk.com/authorize?client_id=6121396&scope=70658&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1";

$version = file_get_contents("version.txt");
$token = readline();

if($token)
{
	$api = new \api\functions($token, 122);
	$status = $api->vk_api("users.get", ["user_ids" => 1]);

	if (json_decode($status)->response[0]->id == 1)
	{
		$data = json_encode(array("token" => $token, "version" => $version));
		$fp = fopen('config.json', 'w');
		fwrite($fp, $data);
		fclose($fp);

		echo "successfully!";
}
else
{
	echo "ERROR: User authorization failed: invalid access_token!";
	}
}
