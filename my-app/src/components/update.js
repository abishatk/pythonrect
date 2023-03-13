import React, { useState,useEffect } from 'react';
import { Button,  Form } from 'semantic-ui-react'
import axios from 'axios';

export default function Update() {
 
    const [company_id, setID] = useState('');
    const [company_name, setCompanyName] = useState('');
    const [year_established,setYear ] = useState('');
    const [type, setType] = useState('');
    const [street_name, setStreetname] = useState('');
    const [city, setCity] = useState('');
    const [Country, setCountry] = useState('');

    const updateAPIData = () => {
        axios.put(`  http://127.0.0.1:8800/update/comp`, {
            company_id,
            company_name,
            year_established,
            type,
            street_name,
            city,
            Country
        })
    }

useEffect(() => {
    setID(localStorage.getItem('Company ID'))
    setCompanyName(localStorage.getItem('Company Name'));
    setYear(localStorage.getItem('Year Established'));
    setType(localStorage.getItem('Type'))
    setStreetname(localStorage.getItem('Street Name'))
    setCity(localStorage.getItem('City'))
    setCountry(localStorage.getItem('_Country'))
}, []);

    return (
        <div>
            <Form className="create-form">
            <Form.Field>
                    <label>Company ID</label>
                    <input placeholder='Company ID' value={company_id} onChange={(e) => setID(e.target.value)}/>
                </Form.Field> 
                <Form.Field>
                    <label>Company Name</label>
                    <input placeholder='Company Name' value={company_name} onChange={(e) => setCompanyName(e.target.value)}/>
                </Form.Field>
                <Form.Field>
                <label>Year Established</label>
                    <input placeholder='Year Established' value={year_established} onChange={(e) => setYear(e.target.value)}/>
                </Form.Field>
                <Form.Field>
                <label>Type</label>
                    <input placeholder='Type' value={type} onChange={(e) => setType(e.target.value)}/>
                </Form.Field>
                <Form.Field>
                <label>Street Name</label>
                    <input placeholder='Street Name' value={street_name} onChange={(e) => setStreetname(e.target.value)}/>
                </Form.Field>
                <Form.Field>
                <label>City</label>
                    <input placeholder='City' value={city} onChange={(e) => setCity(e.target.value)}/>
                </Form.Field>
                <Form.Field>
                <label>Country</label>
                    <input placeholder='Country' value={Country} onChange={(e) => setCountry(e.target.value)}/>
                </Form.Field>
                <Button type='submit' onClick={updateAPIData}>Update</Button>
            </Form>
        </div>
    )
}