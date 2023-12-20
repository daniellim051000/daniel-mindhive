import React, { useState, useEffect } from "react";
import PixiOverlay, {
  MarkersPropsPixiOverlay,
} from "react-leaflet-pixi-overlay";
import { MapContainer, TileLayer } from "react-leaflet";
import axios from "axios";


interface CoffeeShop {
  id: number;
  shop_name: string;
  shop_address: string;
  shop_coordinate_latitude: string;
  shop_coordinate_longitude: string;
}

interface PayloadProps {
  count: number;
  page: number;
  results: CoffeeShop[];
}

function Map() {
  const [shopData, setShopData] = useState<CoffeeShop[]>([]);
  const [markerData, setMarkerData] = useState<MarkersPropsPixiOverlay | null>(
    null
  );

  const BASE_API = process.env.REACT_APP_API_URL;

  useEffect(() => {
    const getCoffeeShopData = async () => {
      try {
        const response = await axios.get<PayloadProps>(
          `${BASE_API}/v1/shop/shop/`
        );
        if (response.data) {
          setShopData(response.data.results);
        }
      } catch (error) {
        console.error("Error fetching shop data:", error);
      }
    };

    if (shopData.length === 0) {
      getCoffeeShopData();
    } else {
      const markers: MarkersPropsPixiOverlay = shopData.map((shop) => ({
        id: shop.id.toString(),
        iconColor: "red", // Modify as needed
        position: [
          parseFloat(shop.shop_coordinate_latitude),
          parseFloat(shop.shop_coordinate_longitude),
        ],
        popup: shop.shop_name,
        popupOpen: true, // Set as needed
        tooltip: "Hey!",
      }));
      setMarkerData(markers);
    }
  }, [BASE_API, shopData]);

  return (
    <MapContainer
      zoom={18} // initial zoom required
      preferCanvas
      maxZoom={20} // required
      minZoom={3} // required
      center={[3.897065497078672, 106.66936701441807]} // get the first item coordinate
      scrollWheelZoom={true}
      // Other map props...
    >
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      {markerData && <PixiOverlay markers={markerData} />}
    </MapContainer>
  );
}

export default Map;
