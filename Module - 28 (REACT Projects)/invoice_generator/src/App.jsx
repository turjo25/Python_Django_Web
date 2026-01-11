import './App.css'
import { useState } from 'react'
import Invoice from './invoice.jsx'
import { PDFViewer,PDFDownloadLink} from '@react-pdf/renderer';
import Product from './Product.jsx';

  const products = [
    { id: 1, name: 'Product A', price: 50, image: 'https://picsum.photos/200/300' },
    { id: 2, name: 'Product B', price: 30, image: 'https://picsum.photos/200/300' },
    { id: 3, name: 'Product C', price: 20, image: 'https://picsum.photos/200/300' },
    { id: 4, name: 'Product D', price: 15, image: 'https://picsum.photos/200/300' },
    { id: 5, name: 'Product E', price: 100, image: 'https://picsum.photos/200/300' },
  ];

function App() {
  const [showPdf, setShowPdf] = useState(false)

  const [selectedProducts, setSelectedProducts] = useState([]);

  function handleSelectProduct(productId) {
    if (selectedProducts.includes(productId)) {
      setSelectedProducts(selectedProducts.filter(id => id !== productId));
    } else {
      setSelectedProducts([...selectedProducts, productId]);
    }
  } 

  function handleShowPdf() {
    setShowPdf(!showPdf)
  }

  function generateInvoiceData() {
    const realSelectedProducts = products.filter(product => selectedProducts.includes(product.id));
    const subtotal = realSelectedProducts.reduce((acc, product) => acc + product.price, 0);//total price of selected products
    const tax = subtotal * 0.1; // Assuming 10% tax rate
    const total = subtotal + tax;

    return {
      invoiceNumber: 'INV-2025-001',
      date: '2025-12-06',
      customerName: 'John Doe',
      customerEmail: 'john.doe@example.com',
      customerAddress: '123 Main Street, New York, NY 10001',
      items: realSelectedProducts.map(product => ({
        id: product.id,
        name: product.name,
        quantity: 1,
        rate: product.price,
        amount: product.price
      })),
      subtotal: subtotal,
      tax: tax,
      total: total

    }

  }
  return (
    <>
    <div>
      <h1 className='text-3xl font-bold underline m-4'>All Products</h1>
      <div className='grid grid-cols-3 gap-4'>
        {
        products.map((product) => (
          <Product key={product.id} product={product} handleSelect={handleSelectProduct} isSelected={selectedProducts.find(id => id === product.id) ? true : false} />
        ))}
      </div>
    </div>



    <button onClick={handleShowPdf} className='mt-6 px-4 py-2 bg-blue-500 text-white rounded m-1.5' cursor='pointer'>
      {showPdf ? "Hide Pdf" : "Show Pdf"}</button>
    <PDFDownloadLink document={<Invoice data = {generateInvoiceData()}/>} fileName="invoice.pdf" className='mt-6 px-4 py-2 bg-blue-500 text-white rounded m-1.5' cursor='pointer'>
      {({ blob, url, loading, error }) =>
        loading ? 'Preparing document...' : 'Download Invoice PDF'
      }
    </PDFDownloadLink>
    {showPdf ? 
    <div className='h-[80vh] w-[700px] mt-6'>
    <PDFViewer showToolbar={true} style={{width: '100%', height: '100%'}}>
      <Invoice data={generateInvoiceData()} />
    </PDFViewer> 
    </div>: null}
    </>
  )
}

export default App
