import axios from "axios";

import BASE_API from './BaseAPI';

export interface StoreResponse{
    id: number;
    shopName: string;
    shopAddress: string;
    shopCoordinateLatitude: number;
    shopCoordinateLongitude: number;
}

export async function getStoreInfo(): Promise<StoreResponse> {
    const url = `${BASE_API}/token/refresh/`;
    const response = await axios.get<StoreResponse>(url);
    return response.data;
}