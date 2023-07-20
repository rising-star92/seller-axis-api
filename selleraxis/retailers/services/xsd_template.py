# flake8: noqa
DEFAULT_XSD_TEMPLATE = """
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- edited with XMLSpy v2017 rel. 3 (x64) (http://www.altova.com) by WIlliam Wood (COMMERCE HUB) -->
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified">
	<xs:element name="advice_file">
		<xs:complexType>
			<xs:sequence>
				<xs:element name="advice_file_control_number" type="xs:string">
					<xs:annotation>
						<xs:documentation>retailer.id</xs:documentation>
					</xs:annotation>
				</xs:element>
				<xs:element name="vendor" type="xs:string">
					<xs:annotation>
						<xs:documentation>vendor</xs:documentation>
					</xs:annotation>
				</xs:element>
				<xs:element ref="vendorMerchID" minOccurs="0">
					<xs:annotation>
						<xs:documentation>retailer.name</xs:documentation>
					</xs:annotation>
				</xs:element>
				<xs:element name="product" maxOccurs="unbounded">
					<xs:annotation>
						<xs:documentation>retailer.retailer_products_aliases.[retailer_products_alias_id]</xs:documentation>
					</xs:annotation>
					<xs:complexType>
						<xs:sequence>
							<xs:element name="vendor_SKU" type="xs:string">
								<xs:annotation>
									<xs:documentation>retailer.retailer_products_aliases.[retailer_products_alias_id].sku</xs:documentation>
								</xs:annotation>
							</xs:element>
							<xs:element name="qtyonhand" type="xs:string">
								<xs:annotation>
									<xs:documentation>retailer.retailer_products_aliases.[retailer_products_alias_id].total_qty_on_hand</xs:documentation>
								</xs:annotation>
							</xs:element>
							<xs:element name="unitOfMeasure" type="xs:string" minOccurs="0">
								<xs:annotation>
									<xs:documentation>retailer.retailer_products_aliases.[retailer_products_alias_id].product.unit_of_measure</xs:documentation>
								</xs:annotation>
							</xs:element>
							<xs:element name="available" type="xs:string">
								<xs:annotation>
									<xs:documentation>retailer.retailer_products_aliases.[retailer_products_alias_id].product.available</xs:documentation>
								</xs:annotation>
							</xs:element>
							<xs:element name="UPC" type="xs:string" minOccurs="0">
								<xs:annotation>
									<xs:documentation>retailer.retailer_products_aliases.[retailer_products_alias_id].product.upc</xs:documentation>
								</xs:annotation>
							</xs:element>
							<xs:element name="description" type="xs:string" minOccurs="0">
								<xs:annotation>
									<xs:documentation>retailer.retailer_products_aliases.[retailer_products_alias_id].product.description</xs:documentation>
								</xs:annotation>
							</xs:element>
							<xs:element name="next_available_date" type="xs:string" minOccurs="0">
								<xs:annotation>
									<xs:documentation>retailer.retailer_products_aliases.[retailer_products_alias_id].next_available_date</xs:documentation>
								</xs:annotation>
							</xs:element>
							<xs:element name="next_available_qty" type="xs:string" minOccurs="0">
								<xs:annotation>
									<xs:documentation>retailer.retailer_products_aliases.[retailer_products_alias_id].next_available_qty</xs:documentation>
								</xs:annotation>
							</xs:element>
							<xs:element name="discontinued_date" type="xs:string" minOccurs="0">
								<xs:annotation>
									<xs:documentation>retailer.retailer_products_aliases.[retailer_products_alias_id].discontinued_date</xs:documentation>
								</xs:annotation>
							</xs:element>
							<xs:element name="unit_cost" type="xs:string" minOccurs="0">
								<xs:annotation>
									<xs:documentation>retailer.retailer_products_aliases.[retailer_products_alias_id].product.unit_cost</xs:documentation>
								</xs:annotation>
							</xs:element>
							<xs:element name="merchantSKU" type="xs:string" minOccurs="0">
								<xs:annotation>
									<xs:documentation>retailer.retailer_products_aliases.[retailer_products_alias_id].merchant_sku</xs:documentation>
								</xs:annotation>
							</xs:element>
							<xs:element name="warehouseBreakout">
								<xs:annotation>
									<xs:documentation>retailer.retailer_products_aliases.[retailer_products_alias_id].retailer_warehouse_products.[retailer_warehouse_product_id]</xs:documentation>
								</xs:annotation>
								<xs:complexType>
									<xs:sequence>
										<xs:element name="warehouse" maxOccurs="unbounded">
											<xs:complexType>
												<xs:sequence>
													<xs:element name="qtyonhand" type="xs:string">
														<xs:annotation>
															<xs:documentation>retailer.retailer_products_aliases.[retailer_products_alias_id].retailer_warehouse_products.[retailer_warehouse_product_id].product_warehouse_statices.qty_on_hand</xs:documentation>
														</xs:annotation>
													</xs:element>
													<xs:element name="next_available" minOccurs="0">
														<xs:annotation>
															<xs:documentation>retailer.retailer_products_aliases.[retailer_products_alias_id].retailer_warehouse_products.[retailer_warehouse_product_id].product_warehouse_statices.next_available_qty</xs:documentation>
														</xs:annotation>
														<xs:complexType>
															<xs:attribute name="quantity" type="xs:string" use="optional">
																<xs:annotation>
																	<xs:documentation>retailer.retailer_products_aliases.[retailer_products_alias_id].retailer_warehouse_products.[retailer_warehouse_product_id].product_warehouse_statices.next_available_qty</xs:documentation>
																</xs:annotation>
															</xs:attribute>
															<xs:attribute name="date" type="xs:string">
																<xs:annotation>
																	<xs:documentation>retailer.retailer_products_aliases.[retailer_products_alias_id].retailer_warehouse_products.[retailer_warehouse_product_id].product_warehouse_statices.next_available_date</xs:documentation>
																</xs:annotation>
															</xs:attribute>
														</xs:complexType>
													</xs:element>
												</xs:sequence>
												<xs:attribute name="warehouse-id" type="xs:string" use="required">
													<xs:annotation>
														<xs:documentation>retailer.retailer_products_aliases.[retailer_products_alias_id].retailer_warehouse_products.[retailer_warehouse_product_id].name</xs:documentation>
													</xs:annotation>
												</xs:attribute>
											</xs:complexType>
										</xs:element>
									</xs:sequence>
								</xs:complexType>
							</xs:element>
						</xs:sequence>
					</xs:complexType>
				</xs:element>
				<xs:element name="advice_file_count" type="xs:string">
					<xs:annotation>
						<xs:documentation>advice_file_count</xs:documentation>
					</xs:annotation>
				</xs:element>
			</xs:sequence>
		</xs:complexType>
	</xs:element>
	<xs:element name="vendorMerchID" type="xs:string">
		<xs:annotation>
			<xs:documentation>retailer.name</xs:documentation>
		</xs:annotation>
	</xs:element>
</xs:schema>
"""
