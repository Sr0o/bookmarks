(function () {
	/*var site_url = 'http://192.168.1.101:8000/static/js/bookmarklet.js?r=';*/
	var site_url = 'http://192.168.43.142:8000/static/js/bookmarklet.js?r=';
	if (window.myBookmarklet !== undefined) {
		myBookmarklet();
	}
	else {
		document.body.appendChild(document.createElement('script')).src=site_url + Math.floor(Math.random() * 99999999999999999999);
	}
})();
