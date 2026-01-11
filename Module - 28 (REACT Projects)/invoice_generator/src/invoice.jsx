import React from 'react';
import { Page, Text, View, Document, StyleSheet } from '@react-pdf/renderer';

// // Create styles
// const styles = StyleSheet.create({
//   page: {
//     flexDirection: 'column',
//     backgroundColor: 'white'
//   },
//   section: {
//     margin: 10,
//     padding: 10,
//     flexGrow: 1
//   }
// });

const styles = StyleSheet.create({
  page: {
    padding: 30,
    backgroundColor: '#ffffff'
  },
  header: {
    fontSize: 24,
    marginBottom: 20,
    textAlign: 'center',
    color: '#2c3e50',
    fontWeight: 'bold'
  },
  section: {
    margin: 10,
    padding: 10,
    borderBottom: '1 solid #e0e0e0'
  },
  sectionTitle: {
    fontSize: 16,
    marginBottom: 10,
    color: '#34495e',
    fontWeight: 'bold'
  },
  text: {
    fontSize: 12,
    marginBottom: 5,
    color: '#555'
  },
  row: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 5
  },
  label: {
    fontSize: 12,
    fontWeight: 'bold',
    color: '#2c3e50'
  },
  value: {
    fontSize: 12,
    color: '#555'
  },
  table: {
    marginTop: 20
  },
  tableRow: {
    flexDirection: 'row',
    borderBottomWidth: 1,
    borderBottomColor: '#e0e0e0',
    paddingVertical: 8
  },
  tableHeader: {
    backgroundColor: '#3498db',
    color: '#ffffff',
    fontWeight: 'bold'
  },
  tableCol: {
    width: '25%',
    paddingHorizontal: 5
  },
  tableCell: {
    fontSize: 10
  },
  footer: {
    marginTop: 30,
    paddingTop: 20,
    borderTop: '2 solid #3498db',
    textAlign: 'center'
  },
  total: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#27ae60',
    textAlign: 'right',
    marginTop: 20
  }
});


// Create Document Component
// const user_name = "John Doe";
const user = {
    name: "John Doe",
    email: "johndoe@gmail.com"
};

// Dummy data
const dummyData = {
  invoiceNumber: 'INV-2025-001',
  date: '2025-12-06',
  customerName: 'John Doe',
  customerEmail: 'john.doe@example.com',
  customerAddress: '123 Main Street, New York, NY 10001',
  items: [
    { id: 1, name: 'Web Development Service', quantity: 40, rate: 75, amount: 3000 },
    { id: 2, name: 'UI/UX Design', quantity: 20, rate: 85, amount: 1700 },
    { id: 3, name: 'Consulting', quantity: 10, rate: 100, amount: 1000 },
    { id: 4, name: 'Project Management', quantity: 15, rate: 90, amount: 1350 }
  ],
  subtotal: 7050,
  tax: 705,
  total: 7755
};


// const Invoice = () => (
//   <Document>
//     <Page size="A4" style={styles.page}>
//       <View style={styles.section}>
//         <Text style={{textAlign:'center'}}>INVOICE</Text>
//         <Text>Bill To: {user.name}</Text>
//         <Text>Bill To: {user.email}</Text>
//         <Text>Item 1: $10.00</Text>
//         <Text>Item 2: $15.00</Text>
//         <Text>Total: $25.00</Text>
//       </View>
//     </Page>
//   </Document>
// );

const Invoice = ({ data = dummyData }) => (
  <Document>
    <Page size="A4" style={styles.page}>
      {/* Header */}
      <Text style={styles.header}>INVOICE</Text>
      
      {/* Invoice Details */}
      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Invoice Details</Text>
        <View style={styles.row}>
          <Text style={styles.label}>Invoice Number:</Text>
          <Text style={styles.value}>{data.invoiceNumber}</Text>
        </View>
        <View style={styles.row}>
          <Text style={styles.label}>Date:</Text>
          <Text style={styles.value}>{data.date}</Text>
        </View>
      </View>

      {/* Customer Details */}
      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Bill To</Text>
        <Text style={styles.text}>{data.customerName}</Text>
        <Text style={styles.text}>{data.customerEmail}</Text>
        <Text style={styles.text}>{data.customerAddress}</Text>
      </View>

      {/* Items Table */}
      <View style={styles.table}>
        {/* Table Header */}
        <View style={[styles.tableRow, styles.tableHeader]}>
          <View style={styles.tableCol}>
            <Text style={styles.tableCell}>Item</Text>
          </View>
          <View style={styles.tableCol}>
            <Text style={styles.tableCell}>Quantity</Text>
          </View>
          <View style={styles.tableCol}>
            <Text style={styles.tableCell}>Rate</Text>
          </View>
          <View style={styles.tableCol}>
            <Text style={styles.tableCell}>Amount</Text>
          </View>
        </View>

        {/* Table Rows */}
        {data.items.map((item) => (
          <View key={item.id} style={styles.tableRow}>
            <View style={styles.tableCol}>
              <Text style={styles.tableCell}>{item.name}</Text>
            </View>
            <View style={styles.tableCol}>
              <Text style={styles.tableCell}>{item.quantity}</Text>
            </View>
            <View style={styles.tableCol}>
              <Text style={styles.tableCell}>${item.rate}</Text>
            </View>
            <View style={styles.tableCol}>
              <Text style={styles.tableCell}>${item.amount}</Text>
            </View>
          </View>
        ))}
      </View>

      {/* Totals */}
      <View style={{ marginTop: 20 }}>
        <View style={styles.row}>
          <Text style={styles.label}>Subtotal:</Text>
          <Text style={styles.value}>${data.subtotal}</Text>
        </View>
        <View style={styles.row}>
          <Text style={styles.label}>Tax (10%):</Text>
          <Text style={styles.value}>${data.tax}</Text>
        </View>
        <Text style={styles.total}>Total: ${data.total}</Text>
      </View>

      {/* Footer */}
      <View style={styles.footer}>
        <Text style={{ fontSize: 10, color: '#7f8c8d' }}>
          Thank you for your business!
        </Text>
        <Text style={{ fontSize: 8, color: '#95a5a6', marginTop: 5 }}>
          Generated by React-PDF on {new Date().toLocaleDateString()}
        </Text>
      </View>
    </Page>
  </Document>
);
export default Invoice;