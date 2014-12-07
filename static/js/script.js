
/**
* Description: Get HTML content for rightpane/content
*
* :param: sGetContent: page to be fetched
*/
function switchMenu(sGetContent) {
    alert("/get_page_content/"+sGetContent);
    $.ajax({
       url: "/get_page_content/"+sGetContent,
       type: "get",
       data: {},
       success: function(response){
           $('#rightpane').html(response)
           alert(response);
       }
    });
    alert('ddd');
};
