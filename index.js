{
    let createPost = function(){
        
        let sendReqButton = $('#getData');

        sendReqButton.click(function(e){
            
            e.preventDefault();

            $.ajax({
                type: 'get',
                url: sendReqButton.attr("href"),
                
                success: function(data){
                    console.log('hello',data);
                    // for(u of data.result)
                    // {
                    // let newitem = newPostDom(u);
                    // $('#post-container>Ol').prepend(newitem);
                    // }
                  
                }, error: function(error){
                    console.log(error.responseText);
                }
            });
        });
    }


    let newPostDom = function(u){
        
        return $(`

    <li style="margin-bottom: 40px;">
                    <table class="table table-hover table-dark" style="width:200%">
                        <tr>
                        
                            <th>
                                Name :
                            </th>
                            <th>
                             Discription :
                            </th>
                            <th>
                                Category :
                            </th>
                            <th>
                                Platform :
                                </th>
                                <th>
                                Location :
                                </th>
                                <th>
                                Date :
                                </th>
                            </tr>
                            
                <tr>
                <td>
                       ${u.username}
                </td>
                <td>
                       ${u.description}
               </td>
                <td>
                       ${u.category}
                </td>
            
                <td>
                       ${u.source}
               </td>
               <td>
                       ${u.location}
               </td>
               <td>
                       ${u.timestamp}
               </td>

            </tr>
                    </table>
                </li>
    
    
    
    
    `)
    
    }
    createPost();
}