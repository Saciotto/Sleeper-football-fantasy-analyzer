import QtQuick
import QtQuick.Window
import QtQuick.Controls

import components

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: qsTr("Sleeper Football Fantasy Analyzer")

    Component.onCompleted: function() {
        app.navigationController.goDashboardView();
    }

    NavigationBar {
        id: navigationBar
        anchors {
            top: parent.top
            bottom: parent.bottom
            left: parent.left
        }
    }

    StackView {
        id: contentFrame
        anchors {
            top: parent.top
            bottom: parent.bottom
            right: parent.right
            left: navigationBar.right
        }
        initialItem: "EmptyView.qml"
        clip: true
    }
}
