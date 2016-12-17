/*
Bones Scripts File
Author: Eddie Machado

This file should contain any js scripts you want to add to the site.
Instead of calling it in the header or throwing it inside wp_head()
this file will be called automatically in the footer so as not to
slow the page load.

*/

// IE8 ployfill for GetComputed Style (for Responsive Script below)
if (!window.getComputedStyle) {
	window.getComputedStyle = function(el, pseudo) {
		this.el = el;
		this.getPropertyValue = function(prop) {
			var re = /(\-([a-z]){1})/g;
			if (prop == 'float') prop = 'styleFloat';
			if (re.test(prop)) {
				prop = prop.replace(re, function () {
					return arguments[2].toUpperCase();
				});
			}
			return el.currentStyle[prop] ? el.currentStyle[prop] : null;
		}
		return this;
	}
}

// as the page loads, call these scripts
jQuery(document).ready(function($) {

	/*
	Responsive jQuery is a tricky thing.
	There's a bunch of different ways to handle
	it, so be sure to research and find the one
	that works for you best.
	*/

	/* getting viewport width */
	var responsive_viewport = $(window).width();

	/* if is below 481px */
	if (responsive_viewport < 481) {

	} /* end smallest screen */

	/* if is larger than 481px */
	if (responsive_viewport > 481) {

	} /* end larger than 481px */

	/* if is above or equal to 768px */
	if (responsive_viewport >= 768) {

		/* load gravatars */
		$('.comment img[data-gravatar]').each(function(){
			$(this).attr('src',$(this).attr('data-gravatar'));
		});

	}

	/* off the bat large screen actions */
	if (responsive_viewport > 1030) {

	}
	$("[title]").tipTip();

	// add all your scripts here

	$('.dropdown-toggle').dropdown();
	$("#gotop").click(function() {
		$("html, body").animate({scrollTop:0}, "200");
	});
	$('#breaking-bar').fadeIn();
	if( $('body').hasClass('rtl')){
		$('#c5-webTicker').webTicker({ direction: "right" });
	}else {
		$('#c5-webTicker').webTicker();
	}
	$(".menu-sc-nav ul.sub-menu li").each(function() {
		if($(this).children("ul.sub-menu").length > 0) {
			if( $('body').hasClass('rtl')){
				$(this).children("a:first").append('<span class="more fa fa-angle-left"></span>');
			}else {
				$(this).children("a:first").append('<span class="more fa fa-angle-right"></span>');
			}
		}
	});
	$(".menu-sc-nav > li").each(function() {
		if($(this).children("ul.sub-menu").length > 0) {
			$(this).children("a:first").append('<span class="more fa fa-angle-down"></span>');
		}
	});
	$(".sidebar .menu-sc-nav > li").each(function() {
		if($(this).children("ul.sub-menu").length > 0) {
			if( $('body').hasClass('rtl')){
				$(this).children("a:first").children('.more').removeClass('fa-angle-down').addClass('fa-angle-left');
			}else {
				$(this).children("a:first").children('.more').removeClass('fa-angle-down').addClass('fa-angle-right');
			}
		}
	});

	//Mega Menu
	$('.c5-mega-menu-li').on('mouseenter', function (e) {

		var $t = $(this);
		if ($t.hasClass('c5-done')) {
			return;
		}
		if($t.parent('.menu-sc-nav').parent('.navigation-shortcode').hasClass('sidebar')){
			return;
		}

		$t.children('.c5-mega-menu-wrap').html('<span class="fa fa-spinner fa-spin c5-loading "></span>');
		$.ajax({
			type: "POST",
			data: 'passing_string=' + $(this).children('a.c5-mega-menu-a').attr('c5-mega-data') + '&action=c5ab_menu_mega_menu',
			url: c5_ajax_var.url,
			success: function (data) {
				$t.children('.c5-mega-menu-wrap').html(data);
				$t.addClass('c5-done');

			}
		});
	});

	$(".navigation-shortcode.responsive-on .responsive-controller").click(function () {
		var menu = $(this).parent().children('ul.menu-sc-nav').clone();


		menu.find('.c5-mega-menu-block').remove();
		menu.find('li').removeClass();
		menu.find('li').css('width','100%');
		menu.find('ul').removeClass();
		menu.removeClass();
		menu.addClass('c5-stroll');
		$.magnificPopup.open({
			items: {
				src: menu
			},
			mainClass: 'c5-menu-post',
			type: 'inline'
		}, 0);

	});

	$(".c5-post-like").click(function(){
		var heart = $(this);
		var post_id = heart.attr("data-post_id");
		$.ajax({
			type: "post",
			url: ajax_var.url,
			data: "action=c5_post_like&nonce="+ajax_var.nonce+"&post_like=&post_id="+post_id,
			success: function(count){
				if(count != "already")
				{
					heart.addClass("voted");
					heart.children('.count').text(count);
				}
			}
		});

		return false;
	});
	$('.c5-mobile-hidden-wrap .top-menu-nav.default ul.menu-sc-nav li.menu-item').click(function(e){
		var this_obj = $(this);
		if ( this_obj.children("ul.sub-menu").length > 0) {
			if (this_obj.hasClass('c5-menu-show')) {
				this_obj.removeClass('c5-menu-show');
				this_obj.addClass('c5-menu-hide');
			}else {
				this_obj.addClass('c5-menu-show');
				this_obj.removeClass('c5-menu-hide');
			}
			e.preventDefault();
		}
	});
	$('.c5-mobile-hidden-wrap .c5-close-mobile-sidebar').click(function(){
		$('.c5-mobile-hidden-wrap').removeClass('c5-mobile-sidebar-show');
	});
	$('.c5-mobile-sidebar').click(function(){
		$('.c5-mobile-hidden-wrap').addClass('c5-mobile-sidebar-show');
	});

	$(".gallery_slider").magnificPopup({
		delegate:	'a',
		type:	'image',
		tLoading: 'Loading image #%curr%...',
		mainClass: 'mfp-img-mobile',
		gallery: {
			enabled: true,
			navigateByImgClick: true,
			preload: [0,1]
		},
		image: {
			tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
			titleSrc: function(item) {
				return item.el.attr('title') + '';
			}
		}
	});

	$('a.woocommerce-main-image').magnificPopup();
	
	$('a.woocommerce-main-image').click(function (e) {
		e.preventDefault();
	});
	
	$(".gallery.flexslider").flexslider({
		animation: "slide",
		slideshowSpeed: 7E3,
		controlNav: true,
	});

	$('#c5_woo_carousel').flexslider({
		animation: "slide",
		controlNav: false,
		animationLoop: false,
		slideshow: false,
		itemWidth: 95,
		itemMargin: 5,
		asNavFor: '#woo_slider'
	});
	$("#woo_slider").flexslider({
		animation: "fade",
		slideshowSpeed: 7E3,
		controlNav: false,
	});


	if ($("#floating-trigger").length > 0) {
		var a = function () {

			var b = $(window).scrollTop();
			var d = $("#floating-trigger").offset().top;
			var c = $("#c5-floating-bar");
			var k = $('.gototop-wtap');
			if (b > d) {
				c.addClass('descended');
				k.fadeIn();
			} else {
				c.removeClass('descended');
				k.fadeOut();
			}

		};
		$(window).scroll(a);
		a();
	}
	$('ul.c5-ss-share li a').click(function(event) {
		event.preventDefault();
		window.open($(this).attr("href"), "popupWindow", "width=600,height=600,scrollbars=yes");
	});


	$('.c5-small-controller ').click(function () {
		if( $('#small-sidebar').hasClass('c5-show') ){
			$('#small-sidebar').removeClass('c5-show');
		}else {
			$('#small-sidebar').addClass('c5-show');
		}
	});
	$('.c5-big-controller ').click(function () {
		if( $('#big-sidebar').hasClass('c5-show') ){
			$('#big-sidebar').removeClass('c5-show');
		}else {
			$('#big-sidebar').addClass('c5-show');
		}
	});

}); /* end of as page load scripts */


/*! A fix for the iOS orientationchange zoom bug.
Script by @scottjehl, rebound by @wilto.
MIT License.
*/
(function(w){
	// This fix addresses an iOS bug, so return early if the UA claims it's something else.
	if( !( /iPhone|iPad|iPod/.test( navigator.platform ) && navigator.userAgent.indexOf( "AppleWebKit" ) > -1 ) ){ return; }
	var doc = w.document;
	if( !doc.querySelector ){ return; }
	var meta = doc.querySelector( "meta[name=viewport]" ),
	initialContent = meta && meta.getAttribute( "content" ),
	disabledZoom = initialContent + ",maximum-scale=1",
	enabledZoom = initialContent + ",maximum-scale=10",
	enabled = true,
	x, y, z, aig;
	if( !meta ){ return; }
	function restoreZoom(){
		meta.setAttribute( "content", enabledZoom );
		enabled = true; }
		function disableZoom(){
			meta.setAttribute( "content", disabledZoom );
			enabled = false; }
			function checkTilt( e ){
				aig = e.accelerationIncludingGravity;
				x = Math.abs( aig.x );
				y = Math.abs( aig.y );
				z = Math.abs( aig.z );
				// If portrait orientation and in one of the danger zones
				if( !w.orientation && ( x > 7 || ( ( z > 6 && y < 8 || z < 8 && y > 6 ) && x > 5 ) ) ){
					if( enabled ){ disableZoom(); } }
					else if( !enabled ){ restoreZoom(); } }
					w.addEventListener( "orientationchange", restoreZoom, false );
					w.addEventListener( "devicemotion", checkTilt, false );
				})( this );
