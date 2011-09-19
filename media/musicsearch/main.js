var api_key = 'U63KOQSGHAHQLGCNE';
var numSongsPlayed = 0;

function testing123() {
	alert('the script is working')
}

function clearBox() {
	document.getElementById('artist_search').value=""
}

function incrementSongsPlayed() {
	numSongsPlayed ++;
	alert(numSongsPlayed);
}

function pullMP3(pickplay) {
	checked = document.getElementById("cycle_checkbox").checked;
	if (pickplay == 0) {
		var artist = document.getElementById("artist_search").value;
	} else if (pickplay==1) {
		var artist = document.getElementById("current_artist").innerHTML;
	} else {
		if (numSongsPlayed == 2 && checked) {
			var artist = document.getElementById("upNext").innerHTML;
			numSongsPlayed = 0;
		} else {
			var artist = document.getElementById("current_artist").innerHTML;
		}
	}

	var numResults = 100
	url = "http://developer.echonest.com/api/v4/artist/audio?callback=?"
	$.getJSON(url, {'api_key':api_key,'name':artist,'results':numResults,'format':'jsonp'},
		function(data) {
			totalSongs = Math.min(data["response"]["total"], numResults);
			var songPick = Math.floor(Math.random()*(totalSongs));
			var mUrl = data["response"]["audio"][songPick]["url"];
			var current_artist = data["response"]["audio"][songPick]["artist"];
			var current_song = data["response"]["audio"][songPick]["title"];
			document.getElementById("current_song").innerHTML = current_song;
			document.getElementById("current_artist").innerHTML = current_artist;
			document.getElementById("song_info_goes_here").style.display = "";
			document.getElementById("audio_player").setAttribute('src', mUrl);
			document.getElementById("audio_player").play();
			document.getElementById('artist_search').value="";
		});
	if (pickplay == 0 || pickplay == 2 && numSongsPlayed == 2 && checked) {
			pullRELATED(pickplay);	
	};
}

function pullRELATED(pickplay) {
	if (pickplay == 0) {
		var artist = document.getElementById("artist_search").value;
	} else {
		var artist = document.getElementById("current_artist").innerHTML;
	}
	var numResults = 20
	url = "http://developer.echonest.com/api/v4/artist/similar?callback=?"
	$.getJSON(url, {'api_key':api_key,'name':artist,'results':numResults,'format':'jsonp'},
		function(data) {
			artistList = data["response"]["artists"];
			totalArtists = artistList.length;
			var artistPick = Math.floor(Math.random()*(totalArtists));
			var simartist = data["response"]["artists"][artistPick]["name"];
			document.getElementById("upNext").innerHTML = simartist;
		});
	
}
