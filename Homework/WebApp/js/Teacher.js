Teacher = {};

Teacher.data = {
    uuid: GlobalConf.uuid,
    Country: "de",
    School: null,
    CreateDate: GlobalConf.today,
    Subjects: null,
    Name: null
}

Teacher.frameSetup = function(parent)
{
    //
    // top div
    //

    var scrollDiv = WebLibSimple.createDiv(0, 0, 0, 0, null, parent);
    // scrollDiv.style.overflow = "auto";
    scrollDiv.style.overflow = "hidden";

    Teacher.topDiv = WebLibSimple.createDiv(20, 20, 20, 20, null, Teacher.scrollDiv);

    var topDiv = Teacher.topDiv;
    topDiv.style.overflow = "auto";
    topDiv.style.fontFamily = "Ubuntu, Helvetica, Arial";
    topDiv.scrollDiv = scrollDiv;

    WebLibSimple.setBGColor(Teacher.topDiv, "#666666");

    // Teacher.topDiv.style.overflow = null;

    //
    // Headline
    //

    // Layout.createHeadline("Teachers", headlineHeight, Teacher.topDiv);

    //
    // top div
    //

    // WebLibSimple.setBGColor(Teacher.topDiv, "#666666");
}

Teacher.dataCallback = function(response)
{
    var parent = WebLibSimple.createDiv(0, 0, 0, 0, null, Teacher.topDiv);
    parent.style.overflow = "auto";
    parent.style.fontFamily = GlobalConf.fontFamily;

    console.log("--> load: " + JSON.stringify(response));
    Data.entrys = response;

    for (var index in Data.entrys)
    {
        Entry.createEntry(Data.entrys[ index ], parent, false);
    }

    Entry.createAddButton(parent);
}

Teacher.main = function(topDiv)
{
    Teacher.topDiv = topDiv;

    window.ondragstart = function() { return false; }
    WebLibSimple.disableSelection(topDiv);
    WebLibSimple.setBGColor(topDiv, GlobalConf.bodyColor);

    //
    // Content
    //

    Elastic.getByUuid("teacher", "PATpLAJgPkDt6iI38jVw", "Teacher.dataCallback");
}

Teacher.main(document.body);
