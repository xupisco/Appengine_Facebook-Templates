var Config = null;
var fb_connected = false;

function facebookInit(config) {
    Config = config;

    FB.init({
        appId: Config.appID,
        xfbml: true,
        status: true,
        channelUrl:
            window.location.protocol + '//' + window.location.host + '/channel.html'
    });
    
    FB.Event.subscribe('auth.statusChange', handleSessionChange);
    FB.Event.subscribe('comment.create', notifyUser);
    
    FB.Canvas.setAutoResize();

    // ensure we're always running on apps.facebook.com
    if (window == top) { goHome(); }
}

function FBLogin() {
    FB.login(function(response) {
        if (!response.authResponse) {
            console.log('Ops... você cancelou ou não autorizou!');
        }
    }, { scope: 'email, publish_stream' });
}

function notifyUser(response) { return false; }

function revokeApp() { // Old REST Method
    FB.api({
        method: 'auth.revokeAuthorization'
    }, function(response) {
        goHome()
    });
}

function handleSessionChange(response) {
    if ((Config.userIDOnServer && !response.authResponse) ||
        Config.userIDOnServer != response.authResponse.userID) {
        goHome();
    }
}

function addAsFriend(uid) {
    FB.ui({
        method: 'friends',
        id: uid,
        message: '### YOUR MSG ###'
    });
}

function inviteFriends() {
    FB.ui({
        method: 'apprequests', 
        message: '### YOUR MSG ###'
    });
}

function sendAppRequest(uid, msg, dest) {
    FB.api('/' + uid +  '/apprequests', 'post', {
        message: msg
    }, function(response) {
        if (!response || response.error) {
            alert('Ops... ERRO enviando request!');
        } else {
            req_info = {
                'req_id': response.request,
                'user_id': uid,
                'redirect_to': dest,
                '_csrf_token': Config.csrf_token
            }
            $.post('/ajax/saveAppRequest', req_info, function(data) {
                if (data != "ok") {
                    alert("Erro salvando informações do request...")
                }
            })
        }
    });
}

function readAppRequests(uid) {
    FB.api('/' + uid + '/apprequests', 'get', function(response) {
        if (!response || response.error) {
            alert('Ops... ERRO!');
        } else {
            alert(response.data.length);
        }
    });
}

function deleteAllAppRequests(uid) {
    FB.api('/' + uid + '/apprequests', 'get', function(response) {
        if (!response || response.error) {
            alert('Ops... ERRO!');
        } else {
            r = response.data
            for (i=0; i < r.length; i++) {
                deleteAppRequest(r[i].id);
            }
        }
    });
}

function deleteAppRequest(req_id) {
    FB.api(req_id, 'delete', function(response) {
        if (!response || response.error) {
            alert('Ops... ERRO!');
        } else {
            alert(req_id + ": deleted...");
        }
    });
}

function goHome() {
    if(!Config.canvasName.indexOf('dev')) {
        top.location = 'http://apps.facebook.com/' + Config.canvasName + Config.content_path;
    }
}

function doSearch(g) {
    $('#qs').val('id:' + g);
    document.location.href = '/offers?qs=id:' + g + '#';
}

function sharePost(offer_id) {
    offer_id = offer_id || false;
    $.getJSON('/ajax/getLatestOfferInfo', { 'offer_id': offer_id }, function(data) {
        FB.ui({
            method: 'stream.publish',
            attachment: {
                name: "### ATTACHMENT NAME ###",
                caption: "### ATTACHMENT CAPTION ###",
                media: [{
                    type: 'image',
                    href: '### IMG HREF ###',
                    src: data.game_box
               }]
            },
            action_links: [{
                text: data.game_name + ' para ' + data.plat_name,
                href: data.application_url + data.offer_url
            }],
            user_message_prompt: '### SHARE PROMPT ###'
            });
        });
}