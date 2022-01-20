function get_img(url) {
    // Add element as a IMAGE
     return '<img src="' + url + '" height="50" width="50"/>';
}

function make_link(res) {
    // Add element as a LINK
     return '<a href="'+ res.url + '">'+ res.name;
}

function add_row(t, data) {
    // Add a row to the Gallery
    t.row.add([
        make_link(data.result),
        get_img(data.result.url)
    ]).draw( false );
}

$(function () {

  $(".js-upload-photos").click(function () {
    $("#fileupload").click();
  });

  $("#fileupload").fileupload({
    dataType: 'json',
    done: function (e, data) {
      if (data.result.is_valid) {
        add_row(t, data)
      }
    }
  });

});
