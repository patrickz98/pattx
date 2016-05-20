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

Teacher.main = function(topDiv)
{
    WebLibSimple.disableSelection(topDiv);
    WebLibSimple.setBGColor(topDiv, GlobalConf.bodyColor);

    //
    // Vars
    //
    // var parent = topDiv;
    var parent = WebLibSimple.createDiv(0, 0, 0, 0, null, topDiv);
    // parent.style.height = "100%";

    parent.style.overflow = "auto";
    parent.style.fontFamily = GlobalConf.fontFamily;

    console.log(parent.scrollTop);
    console.log(parent.scrollHeight);

    var headlineHeight = GlobalConf.headlineHeight;
    var circleSize     = GlobalConf.circleSize;
    var margin         = 40;

    //
    // Center
    //
    // Entry.createEntry(Data.entrys[ 0 ], parent);

    for (var index in Data.entrys)
    {
        Entry.createEntry(Data.entrys[ index ], parent, false);
    }

    // var marginSize  = circleSize + (margin * 2);
    // var addEntry    = WebLibSimple.createDivHeight(0, Entry.getNextEntryStart(), 0, marginSize, null, parent);
    // var center      = WebLibSimple.createAnyAppend("center", addEntry);
    // var backButton  = Layout.createLabelCircle("+", circleSize, GlobalConf.colorFalse, center, Entry.addEntry);
    // backButton.root = addEntry;
    // backButton.topDiv = parent;
}

window.ondragstart = function() { return false; }
Teacher.main(document.body);
