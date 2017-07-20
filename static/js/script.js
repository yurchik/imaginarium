/**
 * Created by yurchik on 7/7/17.
 */
$(document).ready(
  /* This is the function that will get executed after the DOM is fully loaded */
  function () {
      var form = $('#form_check_send');

      function getLike(img_slug, obj_id) {
          var data = {};
          data.slug = img_slug;

          var csrf_token = $('#form_check_send [name="csrfmiddlewaretoken"]').val();
          data["csrfmiddlewaretoken"] = csrf_token;

          var url = form.attr("action");

          // console.log(data);
          var like = $.ajax({
              url: url,
              type: 'POST',
              data: data,
              cache: true,
              success: function (data) {
                  console.log("OK");
                  console.log(data);
                  $('#'+obj_id).parent().next().html(data.like);
              },
              error: function () {
                  console.log("error")
              }
          }).done(function () {
              return data
          });

      }

    $( "body" ).click(function( event ) {
        if (event.target.getAttribute('slug')) {
            getLike(event.target.getAttribute('slug'),event.target.getAttribute('id'))
        }
    });

  }
);