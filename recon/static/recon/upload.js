$(document).ready(function() {

	$('form').on('submit', function(event) {

		event.preventDefault();

		var formData = new FormData($('form')[0]);

		$.ajax({
        
			xhr : function() {
				var xhr = new window.XMLHttpRequest();

				xhr.upload.addEventListener('progress', function(e) {

					if (e.lengthComputable) {

                        if ($('#inputFile').get(0).files.length === 0) {
                            alert("No file found!!")
                        } else {

						console.log('Bytes Loaded: ' + e.loaded);
						console.log('Total Size: ' + e.total);
						console.log('Percentage Uploaded: ' + (e.loaded / e.total))

						var percent = Math.round((e.loaded / e.total) * 100);

						$('#progressBar').attr('aria-valuenow', percent).css('width', percent + '%').text(percent + '%');

					}}

				});

				return xhr;
			},
			type : 'POST',
			url : '/',
			data : formData,
			processData : false,
			contentType : false,
			success : function() {
                console.log("Done")
			}
		});

	});

});

$("button#idGo").click(function() {
    $("div#id_progress").removeAttr("style");
})

$(document).on('click', function showScanBtn() {
    if ($('#inputFile').get(0).files.length === 0) {
        $("div#id_progress").css('display', 'none');
    } else {
        $("button#id_scan").css('display', 'inline');
    }
})

waitForElementToDisplay("#id_progress",function(){showScanBtn()},1000,50000);

function waitForElementToDisplay(selector, callback, checkFrequencyInMs, timeoutInMs) {
  var startTimeInMs = Date.now();
  (function loopSearch() {
    if (document.querySelector(selector) != null && document.getElementById("progressBar").getAttribute("aria-valuenow") == 100) {
      callback();
      return;
    }
    else {
      setTimeout(function () {
        if (timeoutInMs && Date.now() - startTimeInMs > timeoutInMs)
          return;
        loopSearch();
      }, checkFrequencyInMs);
    }
  })();
}

$(document).ready(function() {
    $('button#id_scan').on('click', function () {
        location.href="/scan";
    })
})

$('#id_scan').on('click', function() {
    $('#id_scan').attr("disabled", true);
})