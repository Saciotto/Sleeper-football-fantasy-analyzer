import QtQuick

import assets 1.0

Item {
    property string selectedView: ""

    readonly property string dashboardView: "DashboardView"
    readonly property string bestLineupView: "BestLineupView"
    readonly property string loginView: "LoginView"

    Connections {
        target: masterController.navigationController
        function onGoBestLineupView() {
            selectedView = bestLineupView;
            return contentFrame.replace("qrc:/views/BestLineupView.qml");
        }
        function onGoDashboardView() {
            selectedView = dashboardView;
            if (masterController.navigationController.isLogged) {
                return contentFrame.replace("qrc:/views/DashboardView.qml");
            } else {
                return contentFrame.replace("qrc:/views/LoginView.qml");
            }
        }
        function onGoTeamView() {
            selectedView = loginView;
            return contentFrame.replace("qrc:/views/TeamView.qml");
        }
    }

    width: Style.navigationBarWidth

    Rectangle {
        anchors.fill: parent
        color: Style.navigationBarColor

        Column {
            width: parent.width
            NavigationButton {
                iconCharacter: "\ue871"
                description: qsTr("Dashboard")
                selected: selectedView === dashboardView
                onNavigationButtonClicked: {
                    masterController.navigationController.goDashboardView();
                }
            }
            NavigationButton {
                iconCharacter: "\ue7ef"
                description: qsTr("Team")
                selected: selectedView === loginView
                enabled: masterController.navigationController.isLogged
                onNavigationButtonClicked: {
                    masterController.navigationController.goTeamView();
                }
            }
            NavigationButton {
                iconCharacter: "\ue838"
                description: qsTr("Best Lineup")
                selected: selectedView === bestLineupView
                enabled: masterController.navigationController.isLogged
                onNavigationButtonClicked: {
                    masterController.navigationController.goBestLineupView();
                }
            }
        }
    }
}
