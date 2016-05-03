Menu = {};

Menu.homework = function()
{
    var win = window.open("add.html", "_self");
    win.focus();
}

Menu.teacher = function()
{
    var win = window.open("teacher.html", "_self");
    win.focus();
}

Menu.frameSetup = function()
{
    //
    // borderDiv
    //

    var border = 10;
    Menu.borderDiv = WebLibSimple.createDiv(border, border, border, border, null, document.body);

    //
    // topDiv
    //

    Menu.topDiv = WebLibSimple.createDiv(0, 0, 0, 0, null, Menu.borderDiv);

    //
    // rows
    //

    // var row1 = WebLibSimple.createDiv(0, 0, 0, "50%", null, Layout.topDiv);
    var center = WebLibSimple.createAnyAppend("center", Menu.topDiv);

    // var case1 = WebLibSimple.createDiv(0, 0, "50%", 0, null, row1);

    var size = 200;

    Layout.createMenuPoint("Subjects", size, "#3688d4", center, null);
    Layout.createMenuPoint("Teacher",  size, "#3688d4", center, Menu.teacher);
    Layout.createMenuPoint("Schedule", size, "#3688d4", center, null);
    Layout.createMenuPoint("Homework", size, "#3688d4", center, Menu.homework);
    Layout.createMenuPoint("Task",     size, "#3688d4", center, null);
    Layout.createMenuPoint("School",   size, "#3688d4", center, null);


    // WebLibSimple.setBGColor(row1, "#d45736");

    // var row2 = WebLibSimple.createDiv(0, "50%", 0, 0, null, Layout.topDiv);
    // WebLibSimple.setBGColor(row2, "#3688d4");

    //
    // Headline
    //

    // Layout.createHeadline("Homework Interface", 100, Layout.topDiv);
}

Menu.frameSetup();
