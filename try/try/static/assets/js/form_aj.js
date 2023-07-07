import { log, emailValidator, callAjax, fieldsValidator, removeError, sweetAlertMsg, resetControls, checkAllCheckBoxes } from '../../CommonJS/common.js';


window.removeError = removeError;
window.resetControls = resetControls;


window.Login = async function(_this, username, password, email, profile_img,  user_id)
{
    var email_val = await emailValidator(email);
	if (email_val)
	{
	    var fields = await fieldsValidator([username, password, email, profile_img, user_id]);
        if (fields)
        {

            var fd = new FormData();
            fd.append('username', username);
            fd.append('password', password);
            fd.append('email', email);
            fd.append("profile_img", document.getElementById(profile_img).files[0]);

            var response = await callAjax('/form_save_aj/', fd, null, null, null, true);

            if (response.status == 1)
            {
                alert("success")
                resetControls(['username', 'password','email']);
            }
            else
            {
                alert("error")
            }
        }
    }
}




function getAllInputIds(start, end)
{
    var inputs, index, inputIds, getIds;
    
    inputs = document.getElementsByTagName('input');
    getIds = []
    for (index = 0; index < inputs.length; ++index) {
        inputIds = inputs[index].id
        getIds.push(inputIds)
    }
    return getIds;
}

var starting = $("#starting").text()
var ending = $("#ending").text()

console.log(getAllInputIds(starting, ending))