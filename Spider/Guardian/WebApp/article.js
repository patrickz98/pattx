C3PO = {};

// C3PO.constants.
C3PO.constants =
{
    fontFamily  : "Helvetica",
    breaklineID : "###",
    imgID       : "!!"
};

C3PO.setup = function()
{
    C3PO.topDiv = document.body;

    C3PO.topDivScroll = WebLibSimple.createDiv(0, 0, 0, 0, null, C3PO.topDiv);
    C3PO.topDivScroll.style.overflow = "auto";

    C3PO.globalContainerDiv = WebLibSimple.createDiv(200, 20, 200, 0, null, C3PO.topDivScroll);

    C3PO.httpGet("article.php", C3PO.varSetup);
}

function detectmobile()
{
    if(navigator.userAgent.match(/Android/i)    ||
       navigator.userAgent.match(/webOS/i)      ||
       navigator.userAgent.match(/iPhone/i)     ||
       navigator.userAgent.match(/iPad/i)       ||
       navigator.userAgent.match(/iPod/i)       ||
       navigator.userAgent.match(/BlackBerry/i) ||
       navigator.userAgent.match(/Windows Phone/i)
    )
    {
        console.log("--> Mobile Mod");
        // WebLibSimple.setBGColor(C3PO.topDivScroll, "#00ffff");

        return true;
    }
    else
    {
        return false;
    }
}

C3PO.varSetup = function(json)
{
    json = JSON.parse(json);
    C3PO.json = json;

    if(detectmobile())
    {
        C3PO.textSize = 60;

        C3PO.globalContainerDiv.style.left  = "20px";
        C3PO.globalContainerDiv.style.right = "20px";
    }
    else
    {
        C3PO.textSize = 22;
    }

    C3PO.createTitle(json.trailText);
    C3PO.createBody(json.body);
}

C3PO.createTitle = function(title)
{
    var container = WebLibSimple.createAnyAppend("div", C3PO.globalContainerDiv);
    container.style.paddingBottom = "35px";
    container.style.fontFamily    = C3PO.constants.fontFamily;

    WebLibSimple.setFontSpecs(container, C3PO.textSize, "bold", "#000000");

    var res = title.split(" ");

    for (var word in res)
    {
        var div = WebLibSimple.createAnyAppend("span", container);
        // div.style.display = "inline";
        div.innerHTML     = res[ word ] + " ";
        div.onclick       = C3PO.wordClick;
    }
}

C3PO.createImg = function(src, parent)
{
    var img = document.createElement("img");
    img.src = src;
    img.style.borderRadius = "20px";
    img.style.width  = "100%";
    img.style.height = "auto";

    parent.appendChild(img);
}

C3PO.createBody = function(body)
{
    var container = WebLibSimple.createAnyAppend("div", C3PO.globalContainerDiv);
    container.style.paddingBottom = "45px";
    container.style.fontFamily    = C3PO.constants.fontFamily;

    WebLibSimple.setFontSpecs(container, C3PO.textSize, "lighter", "#000000");

    // console.log(body);

    var res = body.split(" ");

    for (var word in res)
    {
        var part = res[ word ];
        // console.log("Word: " + part);
        // console.log(word.indexOf("Cameron") > -1);

        if (part.indexOf("__VIDEO_") > -1)
        {
            console.log(word);
            console.log("__VIDEO_EMBED_gu-video-");
            continue;
        }

        var imgID = C3PO.constants.imgID
        var regex = new RegExp("^" + imgID + "(.*?)" + imgID + "$", "g");
        var match = part.match(regex);

        if (match)
        {
            var replaceRegex = new RegExp(imgID, "g");
            var replace = part.replace(replaceRegex, "");

            C3PO.createImg(replace, container);
            console.log("Img: " + replace);

            continue;
        }

        if (part == C3PO.constants.breaklineID)
        {
            WebLibSimple.createAnyAppend("br", container);
            WebLibSimple.createAnyAppend("br", container);
            continue;
        }

        var div = WebLibSimple.createAnyAppend("span", container);

        div.innerHTML = part + " ";
        div.onclick   = C3PO.wordClick;
    }
}

C3PO.wordClick = function(event)
{
    word = C3PO.deMoroniseBody(event.target.innerHTML);
    C3PO.httpGet("./pons.php?q=" + word, C3PO.openTranz);

    // console.log(event.target.innerHTML);
}

C3PO.nukeTranz = function()
{
    C3PO.TranzFrame.style.display = "none";
    // C3PO.TranzFrame = null;
}

C3PO.openTranz = function(tranzJson)
{
    console.log(tranzJson);
    // tranzJson = JSON.parse(tranzJson);
    C3PO.TranzFrame = WebLibSimple.createDiv(0, 0, 0, 0, "dimemrDiv", C3PO.topDiv);

    var dimmerDiv     = C3PO.TranzFrame;
    dimmerDiv.onclick = C3PO.nukeTranz;

    WebLibSimple.setBGColor(dimmerDiv, "#66000000");

    var containerDiv = WebLibSimple.createDiv(50, 50, 50, 50, null, dimmerDiv);
    // containerDiv.style.border       = "1px solid black";
    containerDiv.style.borderRadius = "25px";
    containerDiv.style.overflow     = "hidden";
    containerDiv.style.fontFamily   = C3PO.constants.fontFamily;

    WebLibSimple.setBGColor(containerDiv, "#ffffff");

    var contentDiv = WebLibSimple.createDiv(25, 25, 25, 25, null, containerDiv);
    contentDiv.style.overflow = "auto";
    // contentDiv.innerHTML      = tranzJson;

    WebLibSimple.setFontSpecs(contentDiv, C3PO.textSize, "normal", "#000000");

    tranzJson = JSON.parse(tranzJson);

    var word = Object.keys(tranzJson)[ 0 ];

    tranzJson = tranzJson[ word ];

    console.log("--> " + word);

    // var title = WebLibSimple.createDivHeight(0, 0, 0, null, "title", contentDiv);
    var title = WebLibSimple.createAnyAppend("div", contentDiv);
    title.style.paddingBottom = "35px"

    var div = WebLibSimple.createAnyAppend("div", title);
    div.innerHTML = word;
    div.style.borderBottom = "3px dotted #000000";

    WebLibSimple.setFontSpecs(title, C3PO.textSize + 20, "bold", "#000000");

    for (var top in tranzJson)
    {
        for (var trans in tranzJson[ top ])
        {
            var subTitle = WebLibSimple.createAnyAppend("div", contentDiv);
            subTitle.innerHTML = trans;
            WebLibSimple.setFontSpecs(subTitle, C3PO.textSize + 15, "bold", "#000000");

            var div = WebLibSimple.createAnyAppend("div", contentDiv);
            div.innerHTML = tranzJson[ top ][ trans ][ "wordclass" ];
            div.style.fontStyle  = "italic";
            div.style.fontWeight = "lighter";

            // var div = WebLibSimple.createAnyAppend("span", contentDiv);
            // div.innerHTML = JSON.stringify(tranzJson[ top ][ trans ]);

            for (var example in tranzJson[ top ][ trans ][ "translation" ])
            {
                var div = WebLibSimple.createAnyAppend("div", contentDiv);
                div.innerHTML = tranzJson[ top ][ trans ][ "translation" ][ example ][ "source" ];
                div.style.fontWeight = "lighter";

                var div = WebLibSimple.createAnyAppend("div", contentDiv);
                div.innerHTML = tranzJson[ top ][ trans ][ "translation" ][ example ][ "target" ];
                div.style.fontWeight = "lighter";

                WebLibSimple.createAnyAppend("br", contentDiv);
            }

            WebLibSimple.createAnyAppend("br", contentDiv);
            WebLibSimple.createAnyAppend("br", contentDiv);
        }
    }
}

C3PO.httpGet = function(url, event)
{
    var xmlhttp = null;

    if (window.XMLHttpRequest)
    {
        // code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp = new XMLHttpRequest();
    }
    else
    {
        // code for IE6, IE5
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }

    xmlhttp.onreadystatechange = function()
    {
        if ((xmlhttp.readyState == 4) && (xmlhttp.status == 200))
        {
            // console.log(xmlhttp.responseText);

            event(xmlhttp.responseText);

            // return xmlhttp.responseText;
        }
    }

    xmlhttp.open("GET", url, false);
    xmlhttp.send();
}

C3PO.deMoroniseBody = function(body)
{
    body = body.replace(". ", " ");
    body = body.replace("’",  "'");
    body = body.replace("' ",  " ");

    body = body.replace(".",  "");
    body = body.replace(",",  "");
    body = body.replace("\"", "");
    body = body.replace("“",  "");
    body = body.replace("”",  "");
    body = body.replace(":",  "");
    body = body.replace(";",  "");
    body = body.replace("?",  "");
    body = body.replace("!",  "");
    body = body.replace("(",  "");
    body = body.replace(")",  "");
    body = body.replace("[",  "");
    body = body.replace("]",  "");

    return body;
}

C3PO.setup();
