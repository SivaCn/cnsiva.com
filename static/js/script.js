
function get_right_page_content(sDivid, sTargetPage){

    alert('before');
    $.ajax({
        type: "GET",
        url: "~/run.py",
        data: { page_name: 'fdsf' },
        success: function(data) {
            alert('called');
            }
        error: function(error) {
            alert('error');
            }
        });
    alert('after');
    document.getElementById(String(sDivid)).innerHTML = String(sTargetPage);
}
