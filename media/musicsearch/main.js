var api_key = 'U63KOQSGHAHQLGCNE'

function testing123() {
	alert('the script is working')
}

function clearBox() {
	document.getElementById('artist_search').value="";
}

function pullJSON() {
	var artist = document.getElementById("artist_search").value;
	var numResults = 100
	url = "http://developer.echonest.com/api/v4/artist/audio?"
	$.getJSON(url+'api_key='+api_key+'&name='+artist+'&results='+numResults+'&format=jsonp&callback=?', {},
		function(data) {
			totalSongs = Math.min(data["response"]["total"], numResults);
			var songPick = Math.floor(Math.random()*(totalSongs));
			var mUrl = data["response"]["audio"][songPick]["url"];

			var info = data["response"]["audio"][songPick]["artist"]+" - "+data["response"]["audio"][songPick]["title"];
			document.getElementById("response_goes_here").innerHTML = "<span style='color:white;font-size:40px;'>"+info+"</span";
			document.getElementById("audio_player").setAttribute('src', mUrl);
			document.getElementById("audio_player").play();
		});
	

}