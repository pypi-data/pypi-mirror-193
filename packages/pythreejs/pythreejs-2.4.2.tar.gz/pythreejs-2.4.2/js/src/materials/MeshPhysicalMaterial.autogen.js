//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var MeshStandardMaterialModel = require('./MeshStandardMaterial.autogen.js').MeshStandardMaterialModel;


class MeshPhysicalMaterialModel extends MeshStandardMaterialModel {

    defaults() {
        return _.extend(MeshStandardMaterialModel.prototype.defaults.call(this), {

            clearCoat: 0,
            clearCoatRoughness: 0,
            defines: {"PHYSICAL":""},
            reflectivity: 0.5,
            type: "MeshPhysicalMaterial",

        });
    }

    constructThreeObject() {

        var result = new THREE.MeshPhysicalMaterial();
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        MeshStandardMaterialModel.prototype.createPropertiesArrays.call(this);

        this.props_created_by_three['type'] = true;

        this.property_converters['clearCoat'] = 'convertFloat';
        this.property_converters['clearCoatRoughness'] = 'convertFloat';
        this.property_converters['defines'] = null;
        this.property_converters['reflectivity'] = 'convertFloat';
        this.property_converters['type'] = null;

        this.property_assigners['defines'] = 'assignDict';

    }
}

MeshPhysicalMaterialModel.model_name = 'MeshPhysicalMaterialModel';
MeshPhysicalMaterialModel.serializers = {
    ...MeshStandardMaterialModel.serializers,
};

module.exports = {
    MeshPhysicalMaterialModel: MeshPhysicalMaterialModel,
};
