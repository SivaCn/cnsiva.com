
/**
* Description: Get HTML content for rightpane/content
*
* :param: sGetContent: page to be fetched
*/
function switchMenu(sGetContent) {
    $.ajax({
       url: "/get_page_content/"+sGetContent,
       type: "get",
       data: {},
       success: function(response){
           $('#page_content').html(response)
       }
    });
};
