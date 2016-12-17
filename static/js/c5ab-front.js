jQuery(document).ready(function ($) {

	$('[data-animation-name]').each(function(index){
		var b = $(window).scrollTop();
		var a = $(this).offset().top -  $(window).height();
		var animataion = $(this).attr('data-animation-name');
		
		var this_element = $(this);
		var css_code = "";
			
		var delay = this_element.attr("data-animation-delay");
		if(delay){
			css_code += "animation-delay:" + delay + ";";
			css_code += "-webkit-animation-delay:" + delay + ";";
			css_code += "-moz-animation-delay:" + delay + ";";
			css_code += "-ms-animation-delay:" + delay + ";";
			css_code += "-o-animation-delay:" + delay + ";";
		}
		
		var duration = this_element.attr("data-animation-duration");
		if(duration){
			css_code += "animation-duration:" + delay + ";";
			css_code += "-webkit-animation-duration:" + delay + ";";
			css_code += "-moz-animation-duration:" + delay + ";";
			css_code += "-ms-animation-duration:" + delay + ";";
			css_code += "-o-animation-duration:" + delay + ";";
		}
		this_element.attr('style' , css_code);
		
		if(b > a){
			$(this).addClass('showme animated ' +  animataion);
		}
	});
	
	$(window).scroll(function() {
	    $('[data-animation-name]').each(function(index){
	    	var b = $(window).scrollTop();
	    	var a = $(this).offset().top - $(window).height();
	    	var animataion = $(this).attr('data-animation-name');
	    	if(b > a){
	    		$(this).addClass('showme animated ' +  animataion);
	    	}
	    });
	    
	});
	

});