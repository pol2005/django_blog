jQuery(document).ready(function ($) {
$("#c5-submit-newsletter").click(function (e) {
	    if ($("#id_newsemail").val()) {
	        $("#id_newsemail").removeClass("contact_error");
	        var emailReg = /^([\w\-\.]+@([\w\-]+\.)+[\w\-]{2,4})?$/;
	        if (!emailReg.test($("#id_newsemail").val())) {
	            $("#id_newsemail").addClass("contact_error");
	        } else {
	            $.ajax({
	                type: "POST",
	                data: jQuery("#c5-newsletter-form").serialize() + "&action=c5ab_contact_send",
	                url: c5_ajax_var.url,
	                success: function (data) {
	                    if (data === "done") {
	                        $(".message_contact_true").fadeIn();
	                    } else {
	                        $(".message_contact_false").fadeIn();
	                    }
	                }
	            });
	        }
	    } else {
	        if (!$("#id_newsemail").val()) {
	            $("#id_newsemail").addClass("contact_error");
	        } else {
	            $("#id_newsemail").removeClass("contact_error");
	        }
	    }
	    e.preventDefault();
	});
	


});