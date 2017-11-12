$(window).load(function() {
	//We Sell Slider
	$captions = $('.captions');
	$('#buy-slider-container').flexslider({
		animation: "slide",
		pauseOnHover: false,
		directionNav: true,
		slideshowSpeed: 7000,
		animationSpeed: 800,
		controlNav: false,
		keyboard: true,
		useCSS: true,
		prevText: "&#10094;",
		nextText: "&#10095;",
		start: function() {
			$activecaption = $('.flex-active-slide .flex-caption');
			$captions.html($activecaption.text());
		},
		after: function() {
			$activecaption = $('.flex-active-slide .flex-caption');
			$captions.html($activecaption.text());
		}
	});
	//Quote Rotator Slider
	$('#quote-container').flexslider({
		animation: "slide",
		pauseOnHover: false,
		directionNav: true,
		slideshowSpeed: 7000,
		animationSpeed: 800,
		controlNav: false,
		keyboard: false,
		useCSS: true,
		prevText: "&#10094;",
		nextText: "&#10095;",
	});
});

$(document).ready(function() {

	$(document).ajaxStart(function() {
		$('#loading').text('sending...')
	}).ajaxStop(function() { $('#loading').text('')});

	//Smooth Scroll
	$('body a[href*=#]:not([href=#])').click(function() {
		if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') || location.hostname == this.hostname) {

			var target = $(this.hash);
			target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
			if (target.length) {
				$('html,body').animate({
					scrollTop: target.offset().top - 50
				}, 1000);
				return false;
			}
		}
	});
	//Mobile Nav
	$('#mnav-trigger').click(function() {
		$(this).toggleClass('open');
		$('#mobile-nav').slideToggle();
	});
	$('#mobile-nav ul li a').click(function() {
		$('#mobile-nav').slideUp();
	});

	$('#cfg-lead').on('submit', function(evt) {
		evt.preventDefault();
		$("#cfg-lead .pf-error").remove();
		$('#pf-form-error').slideUp('fast', function() {
			$(this).removeClass("success");
		});
		var self = this;
		var textRegEx = /\w{3,}/;
		var stateRegEx = /\w{2,}/;
		var zipRegEx = /(^\d{5}$)|(^\d{5}-\d{4}$)/;
		var hasError = false;
		$('#cfg-lead input[type="text"], #cfg-lead input[type="tel"]').filter('[required]').each(function() {
			var val = $.trim($(this).val());
			var fieldLabel = $(this).prev().text();
			if (this.id == "pf-zip") {
				if (zipRegEx.test(val) == false) {
					$(this).after('<span class="pf-error">The ' + fieldLabel + ' field is not valid.</span>');
					hasError = true;
				}
			} else if (this.id == "pf-state") {
				if (stateRegEx.test(val) == false) {
					console.log("ID: " + this.id + " = " + val);
					$(this).after('<span class="pf-error">The ' + fieldLabel + ' field is not valid.</span>');
					hasError = true;
				}
			} else {
				if (textRegEx.test(val) == false) {
					$(this).after('<span class="pf-error">The ' + fieldLabel + ' field is required.</span>');
					hasError = true;
				}
			}
		});
		if (!$("#pf-term-check").is(":checked")) {
			hasError = true;
			$("#pf-term-check").parent().after('<span class="pf-error terms">You must agree to the terms and conditions.</span>');
		}
		if (!hasError) {
			$.ajax({
				url: "lead.php",
				type: "POST",
				data: $(self).serialize(),
				dataType: "json",
				success: function(data) {
					if (data.error) {
						$('#pf-form-error').text(data.error_msg).show();
						ga('send','event','error',data.error_msg);
					} else {
						$('#pf-form-error').text(data.error_msg).show().addClass("success");
						ga('send','event','packet request','form submit');
						location.href="/thankyou";
					}
				},
				error: function(xhr, status, err) {
					$('#pf-form-error').text(status).show();
				}
			});
		} else {
			$('#pf-form-error').text("Please correct the marked errors below.").show();
		}
	});
	$("#cfg-lead input").on("blur, click", function(evt) {
		$('#pf-form-error').slideUp('fast', function() {
			$(this).removeClass("success");
		});
		if (this.id == "pf-term-check") {
			$(this).parent().next(".pf-error").slideUp('fast', function() {
				$(this).removeClass("success");
			});
		} else {
			$(this).next(".pf-error").slideUp('fast', function() {
				$(this).removeClass("success");
			});
		}
	});

	$(document).on('change','#pf-promo',function(result) {
		var params = {
			method: 'checkpromo',
			promo: $(this).val()
		};
		$.post('/handler.php', params, function(result) {
			$('#pf-promo').removeClass().addClass(result.Status);
		},'json');
	});

	$(document).on('click','#submit-tracking',function(result) {
		var params = {
			method: 'tracking',
			ref: $('#c4g_id').val()
		};
		$.post('/handler.php', params, function(result) {
			$('#main').html(result.Summary[0]);
		},'json');
	});
});
