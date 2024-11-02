from payloads.useragents import generate_headers

cookies = {
    '_ga': 'GA1.1.1051317649.1728700630',
    '__stripe_mid': '0e0e6b2e-75f0-454e-83b2-7f25e83dc4186095f2',
    '__gads': 'ID=dba4702c4773f5b9:T=1728700630:RT=1729075236:S=ALNI_Ma6Qm1qDx-zZeY85s-vNBxidM08pw',
    '__eoi': 'ID=d1c622389d70a306:T=1728700630:RT=1729075236:S=AA-AfjaniKc9k8weeOHi07orqUyM',
    '__stripe_sid': '59ae11fd-1cf4-4b8d-a6da-f4578cf5efd5171406',
    'FCNEC': '%5B%5B%22AKsRol-IWVwipApLfe3wJaGeFVDFXORErO8Y7Mi3kSXUruqpcJYb4PwR2qL4o_K5Me0-pN1r6ZO0lWB8UQ1rFI4UNBc3vkfwq1_iSkP34Ac_BtA9-J0elA4wDBjB-GOAGDYjf-Jxcm_FnwPrEfUld-rUVPRDv_BC_A%3D%3D%22%5D%5D',
    'XSRF-TOKEN': 'eyJpdiI6IjVUa0lUOVFCZVdZVERPcFJ0OVIyMHc9PSIsInZhbHVlIjoicXdCL2FBU3dkK2h0OFpZdE5TbUc1dXoxdmFxUlA2UWZkTFVMcmpsSC92NmZoUS90cFFIUC9HSXdDOEFReXZFL0dLS1pJQW9aTlJPQlExc2dMMmFNZGdIT3FPRGk0Z0dNVkEwSVh3cUVRODJuRG4yM2NnVU91VTVmU25DU2lFanUiLCJtYWMiOiJlNDI4OGIzYjBjY2Q5NTQzZWViMGJmNmJiYjNlMDA1NTk2ZjFkMTQzM2E2MTIxZjgxZGQ1MTIwZjZiMWIxMTNhIiwidGFnIjoiIn0%3D',
    'freefy_session': 'eyJpdiI6IktKRFpkN2ZndWVlVEhTUmpacWlNdUE9PSIsInZhbHVlIjoiMXNtSEt6ZmFJUG94SlRzb2gwNVRVcnBMdnNIUXJPalFRcEZuallCMnFhZjJiL1QwTVlBMlF3eEVVY1puWDJrdjNzclF2RitJSk5pdk1NR3k0TFJXdmlqcWt1QkVpb0duaFZSRkhPUHoyTXlsVjJVcXFmMVRmY3FjRmt2UUJXZlgiLCJtYWMiOiIzNTYyMTZkYTEyMzg4MjQzOGFlNGFiMGUxNWVhYjRiMmVlZWQyNmI2NWUwNmVkZWY4MWIzMDYwYWEzMzdlZDZhIiwidGFnIjoiIn0%3D',
    '_ga_5YJF9KVFPN': 'GS1.1.1729075235.5.1.1729075391.0.0.0',
}

def getHeaders():
    data = generate_headers()
    return {
        'accept': 'application/json',
        'accept-language': 'en-US,en-IN;q=0.9,en;q=0.8,bn;q=0.7',
        'priority': 'u=1, i',
        'referer': 'https://freefy.app/discover',
        'sec-ch-ua': data["sec-ch-ua"],
        'sec-ch-ua-mobile': data["sec-ch-ua-mobile"],
        'sec-ch-ua-platform': data["sec-ch-ua-platform"],
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': data["user-agent"],
        'x-xsrf-token': 'eyJpdiI6IjVUa0lUOVFCZVdZVERPcFJ0OVIyMHc9PSIsInZhbHVlIjoicXdCL2FBU3dkK2h0OFpZdE5TbUc1dXoxdmFxUlA2UWZkTFVMcmpsSC92NmZoUS90cFFIUC9HSXdDOEFReXZFL0dLS1pJQW9aTlJPQlExc2dMMmFNZGdIT3FPRGk0Z0dNVkEwSVh3cUVRODJuRG4yM2NnVU91VTVmU25DU2lFanUiLCJtYWMiOiJlNDI4OGIzYjBjY2Q5NTQzZWViMGJmNmJiYjNlMDA1NTk2ZjFkMTQzM2E2MTIxZjgxZGQ1MTIwZjZiMWIxMTNhIiwidGFnIjoiIn0=',
    }