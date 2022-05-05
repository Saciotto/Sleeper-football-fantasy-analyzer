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

    // Visualization Area
    readonly property color visualizationAreaBackground: secondaryBackgroundColor

    // Editor highlights
    readonly property color keywordHighlightColor: "#45c6d5"
    readonly property color colorHighlightColor: "#ff6aad"
    readonly property color widthHighlightColor: "#d69545"
    readonly property color heightHighlightColor: "#66a334"
    readonly property color horizontalPaddingHighlightColor: "#d69545"
    readonly property color verticalPaddingHighlightColor: "#66a334"
    readonly property color fontHighlightColor: "#4ec9b0"
    readonly property color colorIdHighlightColor: "#4ec9b0"
    readonly property color actionKeyHighlightColor: "#4ec9b0"
    readonly property color imageHighlightColor: "#ff8080"
    readonly property color errorHighlightColor: "#ff0303"

    // Error message
    readonly property color errorMessageBackgroundColor: "#f44336"
    readonly property color errorMessageTextColor: "#ffebee"
    readonly property real errorMessageTextPixSize: 20
    readonly property real errorMessageLabelRadius: 8
    readonly property real errorMessagePadding: 4

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
