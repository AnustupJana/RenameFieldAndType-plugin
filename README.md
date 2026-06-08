# Rename Field and Type QGIS Plugin

![Plugin Icon](https://github.com/AnustupJana/RenameFieldAndType-plugin/blob/main/doc/icon.png?raw=true)

## Overview

The **Rename Field and Type** plugin for QGIS provides a simple and efficient way to rename attribute fields and change their data types within vector layers. Instead of manually creating new fields, copying values, and deleting old fields, users can perform these operations through an easy-to-use graphical interface.

The plugin is designed to streamline attribute table management and improve data preparation workflows for GIS professionals, analysts, surveyors, and cartographers.

## Features

* Rename existing attribute fields.
* Change field data types in a single operation.
* Supports common field types:

  * Text (String)
  * Integer
  * Double
  * Long Integer
  * Boolean
  * Date
  * Time
  * DateTime
  * Binary
* Automatically transfers existing field values.
* Simple and user-friendly interface.
* Works with most editable vector layers.
* Accessible from both the QGIS Toolbar and Plugins Menu.

## Requirements

* **QGIS Version:** 3.0 or later
* **Operating System:**

  * Windows
  * Linux
  * macOS
* **Dependencies:**

  * No external Python libraries required.

## Installation

### 1. From QGIS Plugin Repository

* Open QGIS.
* Go to:

  `Plugins > Manage and Install Plugins`

![Plugin Manager](https://github.com/AnustupJana/RenameFieldAndType-plugin/blob/main/doc/1st.png?raw=true)

* Search for:

  **Rename Field and Type**

* Click **Install Plugin**.

### 2. From ZIP File

* Download the ZIP file from GitHub.

* Open:

  `Plugins > Manage and Install Plugins > Install from ZIP`

* Select the downloaded ZIP file.

* Click **Install Plugin**.

### 3. From Source (Developers)

Clone the repository:

```bash
git clone https://github.com/AnustupJana/RenameFieldAndType-plugin.git
```

Copy the plugin folder to:

**Windows**

```text
C:\Users\<YourUserName>\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins
```

**Linux**

```text
~/.local/share/QGIS/QGIS3/profiles/default/python/plugins
```

**macOS**

```text
~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins
```

### 4. Enable Plugin

* Open QGIS Plugin Manager.
* Search for **Rename Field and Type**.
* Enable the plugin.

### 5. Verify Installation

After installation, the plugin icon will appear in the QGIS toolbar and Plugins menu.

---

## Usage

### 1. Launch the Plugin

Click the **Rename Field and Type** icon from the toolbar.

![Plugin Interface](https://github.com/AnustupJana/RenameFieldAndType-plugin/blob/main/doc/2nd.png?raw=true)

### 2. Select Layer

Choose the vector layer containing the field you want to modify.

### 3. Select Field

Choose the attribute field that needs to be renamed or converted.

### 4. Enter New Field Name

Specify the desired field name.

### 5. Select Field Type

Choose the target field type from the dropdown list.

Supported types include:

* Text (String)
* Integer
* Double
* Long Integer
* Boolean
* Date
* Time
* DateTime
* Binary

### 6. Execute

Click **Rename**.

The plugin will:

1. Create a new field.
2. Copy all existing values.
3. Convert values to the selected type where possible.
4. Remove the original field.
5. Save the changes to the layer.

![Result Example](https://github.com/AnustupJana/RenameFieldAndType-plugin/blob/main/doc/3rd.png?raw=true)

---

## Example

### Before

| Parcel_ID |
| --------- |
| 1001      |
| 1002      |
| 1003      |

### Rename To

Field Name:

```text
PID
```

Field Type:

```text
Text (String)
```

### Result

| PID  |
| ---- |
| 1001 |
| 1002 |
| 1003 |

---

## Development

**Author:** Anustup Jana

**Email:** [anustupjana21@gmail.com](mailto:anustupjana21@gmail.com)

**Version:** 1.0

**Started:** June 2026

**License:** GNU General Public License v2.0 or later

---

## Known Limitations

* The layer must support editing.
* Some data type conversions may result in NULL values if conversion is not possible.
* Very large datasets may take longer to process.

---

## Issues and Support

Found a bug or have a feature request?

Please create an issue on GitHub:

https://github.com/AnustupJana/RenameFieldAndType-plugin/issues

For direct queries:

[anustupjana21@gmail.com](mailto:anustupjana21@gmail.com)

---

## License

This plugin is licensed under the **GNU General Public License v2.0 or later**.

See the [LICENSE](https://github.com/AnustupJana/RenameFieldAndType-plugin/blob/main/LICENSE) file for more information.
