pragma Singleton

import QtQuick 6.1
import QtQuick.Controls.Material 6.1

Item {
    // General
    readonly property color backgroundColor: "#181c28"
    readonly property color secondaryBackgroundColor: "#1f2431"

    // Navigation Bar
    readonly property color navigationBarColor: secondaryBackgroundColor
    readonly property real navigationBarWidth: 80

    // Navigation Button
    readonly property color navigationButtonColor: navigationBarColor
    readonly property color navigationButtonPressedColor: "#262d3c"
    readonly property color navigationButtonSelectionIndicatorColor: "#00ceb8"
    readonly property color navigationButtonHoveredColor: navigationButtonPressedColor
    readonly property real navigationButtonHeight: 80
    readonly property real navigationButtonIconPixSize: 38
    readonly property real navigationButtonTextPixSize: 12
    readonly property real navigationButtonSpacing: 4

    // Player
    readonly property color qbBackgroundColor: "#ff2a6d"
    readonly property color wrBackgroundColor: "#58a7ff"
    readonly property color rbBackgroundColor: "#00ceb8"
    readonly property color teBackgroundColor: "#ffae58"
    readonly property color dlBackgroundColor: "#ff795a"
    readonly property color lbBackgroundColor: "#6d7df5"
    readonly property color dbBackgroundColor: "#ff7cb6"
    readonly property color genericBackgroundColor: "#2c3749"

    // Fonts
    property alias fontAwesome: fontAwesomeLoader.name
    property alias fontMaterialIcons: fontMaterialIconsLoader.name
    property alias fontMonospace: fontMonospaceLoader.name

    FontLoader {
        id: fontAwesomeLoader
        source: "qrc:/assets/fontawesome.ttf"
    }

    FontLoader {
        id: fontMaterialIconsLoader
        source: "qrc:/assets/material-icons.ttf"
    }

    FontLoader {
        id: fontMonospaceLoader
        source: "qrc:/assets/DejaVuSansMono.ttf"
    }
}
