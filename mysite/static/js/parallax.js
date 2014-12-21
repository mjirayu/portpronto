$(document).ready(function (){

	$(window).bind('scroll', function(e){
		parallax();
	});

	$('a.about').click(function() {

		$('html, body').animate({ scrollTop:0 }, 1000, 
			function(){
				parallax();
			});
		return false;

	});

	$('a.activities').click(function() {

		$('html, body').animate({ scrollTop:$('section#activities').offset().top }, 1000, 
			function(){
				parallax();
			});
		return false;

	});

	$('a.contact').click(function() {

		$('html, body').animate({ scrollTop:$('section#contact').offset().top }, 1000, 
			function(){
				parallax();
			});
		return false;

	});

});


function parallax() {
	var scrollPosition = $(window).scrollTop();
	$('#stars').css('top', (0 - (scrollPosition * .2) ) + 'px');
	$('#images').css('top', (0 - (scrollPosition * .5) ) + 'px');
}