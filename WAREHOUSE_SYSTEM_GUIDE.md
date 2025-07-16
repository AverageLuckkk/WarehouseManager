# 🏭 Warehouse & Logistics Management System

## Overview
A comprehensive web-based warehouse and logistics management system built with Flask and SQLite. This application provides efficient inventory management across multiple storage locations with a modern, user-friendly interface.

## ✨ Key Features

### 🏗️ **Storage Locations**
The system comes pre-configured with your requested storage locations:

**Bulk Storage Areas:**
- Bulk 1 - Bulk 6 (6 locations)
- Color-coded in **purple** for easy identification

**Miscellaneous Storage Areas:**
- Miscellaneous 1 - Miscellaneous 2 (2 locations)  
- Color-coded in **teal** for easy identification

**Side Storage Areas:**
- Side 1 - Side 2 (2 locations)
- Color-coded in **orange** for easy identification

### 📦 **Inventory Management**
- **Add Items**: Create new inventory items with name, quantity, and additional information
- **Edit Items**: Modify existing item details including name, ID, quantity, and notes
- **Quick Quantity Adjustments**: Buttons for ±1 and ±10 quantity changes
- **Delete Items**: Remove items from inventory with confirmation
- **Real-time Statistics**: View total items and quantities per location

### 🎨 **Modern Interface**
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Color-coded Locations**: Visual differentiation between storage area types
- **Interactive Elements**: Hover effects and smooth transitions
- **Professional Styling**: Modern gradient backgrounds and clean typography
- **Empty State Messages**: Helpful guidance when locations are empty

## 🚀 How to Use

### 1. **Starting the Application**
```bash
python3 app.py
```
The application will be available at: `http://127.0.0.1:5000/`

### 2. **Navigating Storage Locations**
- Use the **Storage Locations** panel on the left sidebar
- Click any location button to switch between storage areas
- Current location is displayed at the top of the sidebar

### 3. **Managing Inventory**

#### Adding Items:
1. Select your desired storage location
2. Fill out the "Add New Item" form:
   - **Item Name**: Product or item name
   - **Quantity**: Number of items (numerical input)
   - **Other Information**: Additional details, notes, or specifications
3. Click "➕ Add Item"

#### Editing Items:
1. In the inventory table, click "✏️ Edit" for the desired item
2. Modify the details in the form that appears
3. Click "💾 Save Changes"

#### Adjusting Quantities:
- Use the quantity control buttons in each row:
  - **-10** and **-1**: Decrease quantity
  - **+1** and **+10**: Increase quantity

#### Deleting Items:
1. Click "🗑️ Delete" for the item you want to remove
2. Confirm the deletion in the popup dialog

### 4. **Adding New Storage Locations**
1. In the sidebar, use the "Add New Location" form
2. Enter the location name
3. Optionally check "Copy items from current location" to duplicate item types
4. Click "Add Location"

### 5. **Deleting Storage Locations**
1. Select the location you want to delete
2. Click "Delete Current Location" (red button)
3. Confirm the deletion

## 📊 **Sample Data Included**

The system comes with realistic sample inventory data:

**Bulk Storage Examples:**
- Pallets, Steel Beams, Concrete Blocks, Lumber, Pipes, Wire Spools

**Miscellaneous Storage Examples:**
- Safety Vests, Hard Hats, Tool Boxes, Extension Cords, Work Gloves, First Aid Kits

**Side Storage Examples:**
- Spray Paint, Cleaning Supplies, Office Supplies, Computer Equipment, Small Parts, Maintenance Tools

## 🛠️ **Technical Details**

### **Technology Stack:**
- **Backend**: Python 3 with Flask framework
- **Database**: SQLite for persistent data storage
- **Frontend**: HTML5, CSS3 with modern styling
- **Responsive Design**: CSS Grid and Flexbox

### **File Structure:**
```
warehouse-management/
├── app.py                    # Main Flask application
├── warehouse_manager.py      # Database management logic
├── setup_warehouses.py      # Initial location setup
├── add_sample_data.py       # Sample inventory data
├── templates/
│   └── index.html           # Main web interface
├── default_database         # SQLite database file
└── README.txt              # Basic setup instructions
```

### **Database Schema:**
- Each storage location is a separate table
- Columns: name, id (auto-increment), quantity, other
- SQLite handles data persistence

## 🔧 **Setup Requirements**

### **Dependencies:**
- Python 3.x
- Flask web framework

### **Installation:**
```bash
# Install Flask
pip3 install --break-system-packages flask

# Set up storage locations
python3 setup_warehouses.py

# Add sample data (optional)
python3 add_sample_data.py

# Start the application
python3 app.py
```

## 🌟 **Advanced Features**

### **Search and Filter** (Future Enhancement)
The system is designed to easily accommodate search and filtering capabilities.

### **Reporting** (Future Enhancement)
The data structure supports generating inventory reports and analytics.

### **User Management** (Future Enhancement)
The architecture can be extended to include user authentication and role-based access.

### **API Integration** (Future Enhancement)
The Flask backend can easily expose REST APIs for integration with other systems.

## 🚨 **Important Notes**

1. **Data Persistence**: All data is stored in the SQLite database file (`default_database`)
2. **Backup**: Regularly backup the database file to prevent data loss
3. **Concurrent Access**: The current setup is designed for single-user operation
4. **Security**: This is a development server - use proper WSGI server for production

## 📈 **Usage Tips**

1. **Organization**: Use the color-coded storage areas to organize different types of inventory
2. **Naming**: Use descriptive item names for easy identification
3. **Documentation**: Utilize the "Other Information" field for important details
4. **Regular Updates**: Keep quantities current for accurate inventory tracking
5. **Batch Operations**: Use the ±10 buttons for faster quantity adjustments

## 🆘 **Troubleshooting**

### **Application Won't Start:**
- Ensure Flask is installed: `python3 -c "import flask"`
- Check for port conflicts on 5000
- Verify all files are in the same directory

### **Database Issues:**
- Delete `default_database` file and re-run setup scripts
- Check file permissions in the working directory

### **Interface Issues:**
- Clear browser cache and refresh
- Ensure JavaScript is enabled
- Try a different browser

---

## 🎯 **Your Warehouse System is Ready!**

Your warehouse and logistics management system is now fully operational with:
- ✅ 6 Bulk storage locations (Bulk 1-6)
- ✅ 2 Miscellaneous storage locations (Miscellaneous 1-2)  
- ✅ 2 Side storage locations (Side 1-2)
- ✅ Modern, professional web interface
- ✅ Complete inventory management functionality
- ✅ Sample data for immediate testing

**Access your system at: http://127.0.0.1:5000/**

Enjoy managing your warehouse inventory efficiently! 🚀