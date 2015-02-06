
/**
* Description:
*
*/
function showMainPage() {
    $.ajax({
       url: "/show_main_page",
       type: "get",
       data: {},
       success: function(response){
           $('#page_content').html(response)
       }
    });
};


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

/**
* Description: Get HTML content for rightpane/content
*
* :param: sGetContent: page to be fetched
*/
function getQuotes() {
    $.ajax({
       url: "/get_quotes",
       type: "get",
       data: {},
       success: function(response){
           $('#page_content').html(response)
       }
    });
};
