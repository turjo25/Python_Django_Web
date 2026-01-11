function Product({ product,isSelected,handleSelect }) {
  return (
    <div className="relative border p-4 rounded shadow cursor-pointer">
      <input  checked={isSelected} onChange={() => handleSelect(product.id)} type="checkbox" className="mb-2 absolute top-4 right-4 cursor-pointer" />
      <img src={product.image} alt={product.name} className="w-full h-48 object-cover mb-4" />
      <h2 className="text-xl font-bold mb-2">{product.name}</h2>
      <p className="text-gray-700 mb-2">Price: ${product.price}</p>
    </div>
  );
}

export default Product;