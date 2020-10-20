function incrementCount() {
	var d1 = document.getElementById('visits');
	const visits = fetch('https://api.livialima.net/') //please use your own api here
		.then(res => res.json())
		.then(data => d1.insertAdjacentText('beforeend', data))
		.catch(error => console.log(error))
}
